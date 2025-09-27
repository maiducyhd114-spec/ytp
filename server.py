cat > server.py <<'PY'
#!/usr/bin/env python3
from flask import Flask, redirect, jsonify
import os

app = Flask(__name__)

# SĐT -> link YouTube (đổi URL nếu muốn video cụ thể)
KEYS = {
    "0388486866": "https://m.youtube.com",
    # "0962490333": "https://m.youtube.com/watch?v=VIDEO_ID",
}

@app.route("/")
def home():
    return "✅ Server OK. Dùng: /<sdt>  (VD: /0388486866)"

@app.route("/<sdt>")
def open_by_phone(sdt: str):
    url = KEYS.get(sdt)
    if not url:
        return jsonify(ok=False, reason="invalid_phone"), 404
    return redirect(url, code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
PY
