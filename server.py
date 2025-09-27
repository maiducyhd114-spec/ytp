# server.py
from flask import Flask, redirect

app = Flask(__name__)

# Map SĐT -> link YouTube (có thể thêm nhiều số)
KEYS = {
    "0388486866": "https://www.youtube.com/",
    "0912345678": "https://www.youtube.com/",
    # Thêm số khác vào đây...
}

@app.route("/")
def home():
    return "✅ Server OK – nhập số điện thoại vào URL (VD: /0388486866)"

@app.route("/<phone>")
def open_phone(phone):
    url = KEYS.get(phone)
    if url:
        return redirect(url)
    return "❌ SĐT không hợp lệ!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
