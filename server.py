from flask import Flask, redirect

app = Flask(__name__)

# Trang chủ để test nhanh
@app.route("/")
def home():
    return "✅ Server chạy OK - nhập số điện thoại vào URL để test."

# Map số điện thoại (key) sang link YouTube
phone_map = {
    "0388486866": "https://www.youtube.com/"
}

@app.route("/<phone>")
def open_link(phone):
    if phone in phone_map:
        return redirect(phone_map[phone])
    return "❌ Key không hợp lệ!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
