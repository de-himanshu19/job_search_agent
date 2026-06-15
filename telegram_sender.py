import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_message(message):
    if not BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is missing in .env file")

    if not CHAT_ID:
        raise ValueError("TELEGRAM_CHAT_ID is missing in .env file")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "disable_web_page_preview": True
    }

    response = requests.post(url, data=payload, timeout=20)

    if response.status_code == 200:
        print("Telegram message sent successfully.")
        return True
    else:
        print("Failed to send Telegram message.")
        print(response.text)
        return False