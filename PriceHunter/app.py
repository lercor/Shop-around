from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from modules.url_generator import build_platform_links, normalize_query
from modules.data_processor import save_search, get_recent_searches
import os
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "pricehunter-demo-secret-change-me"
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", searches=get_recent_searches())

@app.route("/search", methods=["POST"])
def search():
    raw_query = request.form.get("query", "").strip()
    product_url = request.form.get("product_url", "").strip()
    uploaded = request.files.get("product_image")
    image_path = None

    if uploaded and uploaded.filename:
        if not allowed_file(uploaded.filename):
            flash("圖片格式不支援，請使用 JPG、PNG 或 WEBP。", "error")
            return redirect(url_for("index"))
        ext = uploaded.filename.rsplit(".", 1)[1].lower()
        filename = secure_filename(f"{uuid4().hex}.{ext}")
        uploaded.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        image_path = url_for("static", filename=f"uploads/{filename}")

    query = normalize_query(raw_query, product_url)
    if not query:
        flash("請輸入商品關鍵字或商品網址。若只上傳圖片，請再補充商品名稱或關鍵字。", "error")
        return redirect(url_for("index"))

    links = build_platform_links(query)
    save_search(query, product_url, image_path)
    return render_template(
        "results.html",
        query=query,
        product_url=product_url,
        image_path=image_path,
        links=links,
        searches=get_recent_searches()
    )

@app.errorhandler(413)
def too_large(_error):
    flash("圖片太大，請上傳 8MB 以下的圖片。", "error")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
