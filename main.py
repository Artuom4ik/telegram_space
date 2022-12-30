import os

import telegram 
from dotenv import load_dotenv


def telegram_bot():
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    api_bot = os.getenv("API_BOT")
    bot = telegram.Bot(token=api_bot)
    updates = bot.get_updates()
    bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_1.jpg', 'rb'))


if __name__ == "__main__":
    telegram_bot()
