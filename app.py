# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# For development you can allow all origins. In production, restrict to your domain:
# CORS(app, origins=["https://your-site.com"])
CORS(app)

@app.route("/")
def home():
    return "Chatbot is live"

@app.route("/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    user_msg = (payload.get("message") or "").strip()

    if not user_msg:
        return jsonify({"reply": "Please type a message."})

    # very simple rule-based replies (replace with your logic / AI calls)
    lower = user_msg.lower()
    if "price" in lower or "pricing" in lower:
        reply = "Our basic plan starts at ₹499/month. Want details?"
    elif "hello" in lower or "hi" in lower:
        reply = "Hi! How can I help you today?"
    else:
        reply = f"I heard: {user_msg}"

    return jsonify({"reply": reply})
