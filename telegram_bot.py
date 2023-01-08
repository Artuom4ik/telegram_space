import os

import telegram
from dotenv import load_dotenv


def telegram_bot(chat_id, api_bot):
    bot = telegram.Bot(token=api_bot)
    
    bot.send_document(chat_id=chat_id, document=image)


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    api_bot = os.getenv("API_BOT")
    telegram_bot(chat_id, api_bot)
