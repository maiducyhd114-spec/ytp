from flask import Flask, redirect

app = Flask(__name__)

# Danh sách key hợp lệ (ở đây ví dụ là số điện thoại)
KEY_MAP = {
    "0388486866": "https://www.youtube.com/",
    "0987654321": "https://www.youtube.com/",
    "0909999999": "https://www.youtube.com/"
}

@app.route("/")
def home():
    return "✅ Server chạy OK - nhập số điện thoại vào URL để test."

@app.route("/<key>")
def open_key(key):
    # Nếu key tồn tại trong KEY_MAP thì redirect
    if key in KEY_MAP:
        return redirect(KEY_MAP[key])
    return "❌ Key không hợp lệ!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
