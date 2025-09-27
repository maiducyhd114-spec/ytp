from flask import Flask, redirect, jsonify
import os

app = Flask(__name__)

# SĐT -> URL cần mở
KEYS = {
    "0388486866": "https://www.youtube.com/",
    # thêm số khác ở đây nếu muốn
}

@app.route("/")            # Trang chủ test nhanh
def home():
    return "✅ Server OK. Dùng: /<sdt>  (ví dụ: /0388486866)"

@app.route("/<sdt>")       # Nhập trực tiếp số điện thoại
def open_phone(sdt: str):
    url = KEYS.get(sdt)
    if not url:
        return jsonify(ok=False, reason="invalid_phone"), 404
    return redirect(url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
