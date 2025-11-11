import os
from flask import Flask, request, jsonify
import requests
from core.db import init_db
from core.ai_advisor import get_budget_advice

app = Flask(__name__)
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"

init_db()

def send_message(chat_id, text, reply_markup=None):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    if reply_markup:
        payload["reply_markup"] = reply_markup
    requests.post(API_URL + "sendMessage", json=payload)

@app.route("/api/bot_webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    message = data.get("message") or {}
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if not chat_id:
        return jsonify({"ok": False})

    if text == "/start":
        send_message(chat_id, "Привет! Открой приложение для управления финансами:", 
            reply_markup={
                "inline_keyboard":[[{"text":"Открыть Финансы","web_app":{"url":"https://YOUR_VERCEL_APP/webapp/index.html"}}]]
            })
        return jsonify({"ok": True})

    if text.lower() == "совет":
        advice = get_budget_advice(chat_id)
        send_message(chat_id, advice)
        return jsonify({"ok": True})

    return jsonify({"ok": True})
