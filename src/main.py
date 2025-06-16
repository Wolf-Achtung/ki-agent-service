import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from crew_config import crew
import requests

load_dotenv()

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    result = crew.run({"questionnaire": data})
    # optional an PDFMonkey posten...
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
