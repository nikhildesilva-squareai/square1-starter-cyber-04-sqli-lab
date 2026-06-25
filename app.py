"""
The bundled DELIBERATELY VULNERABLE app for the SQL Injection Lab.

  python app.py        # serves on http://127.0.0.1:5000

AUTHORIZED USE ONLY. This app is intentionally insecure and exists solely as the
local target for THIS lab. Run it on your own machine, attack only this app, and
never deploy it or expose it beyond 127.0.0.1.

It builds SQL by STRING CONCATENATION on purpose (the bug you will exploit, then
fix). Two surfaces:
  POST /login        form: username, password   -> vulnerable to auth bypass
  GET  /search?q=    query string                -> leaks internal (listed=0) rows

Your job (see brief): exploit it, then rewrite get_user / search_products to use
parameterized queries + allow-listing so the payloads in dataset/payloads.csv
stop working. Use sqli.is_query_safe / parameterize_query as you go.

The app loads dataset/app.db (run `python generate_dataset.py` from the project
root first). If it isn't found, it builds a tiny fallback so the app still runs.
"""
from __future__ import annotations

import os
import sqlite3

from flask import Flask, request, jsonify

app = Flask(__name__)

# Resolve dataset/app.db relative to this file's parent (the project root).
HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "dataset", "app.db")


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    return conn


def ensure_db() -> None:
    """If dataset/app.db is missing, build a minimal stand-in so the app runs."""
    if os.path.exists(DB_PATH):
        return
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(
        """
        CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT,
                            role TEXT, secret TEXT);
        CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT,
                               price REAL, listed INTEGER);
        INSERT INTO users VALUES
          (1,'admin','S0meAdminPass!42','admin','FLAG_sq1_EXAMPLE_admin_secret_not_a_real_key_REPLACE'),
          (2,'ava.kim','hunter2pw','user',NULL);
        INSERT INTO products VALUES
          (1,'Widget Model 101','Widgets',12.5,1),
          (2,'Internal Gadget 900','Gadgets',99.0,0);
        """
    )
    conn.commit()
    conn.close()


# --- VULNERABLE query helpers (string concatenation). FIX THESE. -------------

def get_user(username: str, password: str):
    """VULNERABLE login lookup — concatenates user input straight into SQL."""
    conn = get_conn()
    query = ("SELECT id, username, role, secret FROM users "
             "WHERE username = '" + username + "' AND password = '" + password + "'")
    try:
        rows = conn.execute(query).fetchall()
    finally:
        conn.close()
    return rows


def search_products(term: str):
    """VULNERABLE product search — concatenates the term, leaks listed=0 rows."""
    conn = get_conn()
    query = ("SELECT id, name, category, price, listed FROM products "
             "WHERE listed = 1 AND name LIKE '%" + term + "%'")
    try:
        rows = conn.execute(query).fetchall()
    finally:
        conn.close()
    return rows


# --- routes ------------------------------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    try:
        rows = get_user(username, password)
    except sqlite3.Error as e:
        # Verbose errors are themselves a vulnerability (error-based SQLi).
        return jsonify({"ok": False, "error": str(e)}), 500
    if rows:
        user = rows[0]
        return jsonify({"ok": True, "username": user[1], "role": user[2], "secret": user[3]})
    return jsonify({"ok": False}), 401


@app.route("/search", methods=["GET"])
def search():
    term = request.args.get("q", "")
    try:
        rows = search_products(term)
    except sqlite3.Error as e:
        return jsonify({"ok": False, "error": str(e)}), 500
    products = [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]
    return jsonify({"ok": True, "count": len(products), "products": products})


@app.route("/")
def index():
    return (
        "SQL Injection Lab — bundled vulnerable app (authorized testing only).\n"
        "POST /login (username, password) | GET /search?q=...\n"
    )


if __name__ == "__main__":
    ensure_db()
    # 127.0.0.1 only — never expose this intentionally-vulnerable app.
    app.run(host="127.0.0.1", port=5000, debug=True)
