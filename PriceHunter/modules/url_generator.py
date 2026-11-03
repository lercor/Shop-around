from urllib.parse import quote_plus, urlparse
import re

PLATFORMS = [
    {"name": "Shopee 蝦皮", "key": "shopee", "template": "https://shopee.tw/search?keyword={q}", "note": "台灣站商品搜尋"},
    {"name": "Taobao 淘寶", "key": "taobao", "template": "https://s.taobao.com/search?q={q}", "note": "淘寶商品搜尋"},
    {"name": "momo 購物網", "key": "momo", "template": "https://www.momoshop.com.tw/search/searchShop.jsp?keyword={q}", "note": "台灣站商品搜尋"},
    {"name": "Tmall 天貓", "key": "tmall", "template": "https://list.tmall.com/search_product.htm?q={q}", "note": "天貓商品搜尋"},
    {"name": "Pinduoduo 拼多多", "key": "pinduoduo", "template": "https://mobile.yangkeduo.com/search_result.html?search_key={q}", "note": "拼多多搜尋入口"},
]

def normalize_query(query, product_url=""):
    query = (query or "").strip()
    if query:
        return re.sub(r"\s+", " ", query)
    if product_url:
        parsed = urlparse(product_url if "://" in product_url else "https://" + product_url)
        host = parsed.netloc.replace("www.", "")
        return host or product_url
    return ""

def build_platform_links(query):
    encoded = quote_plus(query)
    return [
        {**platform, "url": platform["template"].format(q=encoded)}
        for platform in PLATFORMS
    ]
