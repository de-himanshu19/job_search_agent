import os
import requests
from dotenv import load_dotenv

# Load variables from .env file
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
        "text": message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Failed to send message.")
        print(response.text)


if __name__ == "__main__":
    test_message = "Hello Himanshu! Your Job Search Agent Telegram setup is working."
    send_telegram_message(test_message)