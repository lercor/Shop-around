import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("database", "products.db")
os.makedirs("database", exist_ok=True)

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS searches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                product_url TEXT,
                image_path TEXT,
                created_at TEXT NOT NULL
            )
        """)

def save_search(query, product_url="", image_path=None):
    init_db()
    with connect() as conn:
        conn.execute(
            "INSERT INTO searches (query, product_url, image_path, created_at) VALUES (?, ?, ?, ?)",
            (query, product_url, image_path, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )

def get_recent_searches(limit=8):
    init_db()
    with connect() as conn:
        rows = conn.execute(
            "SELECT query, created_at FROM searches ORDER BY id DESC LIMIT ?", (limit,)
        ).fetchall()
    return [dict(row) for row in rows]
