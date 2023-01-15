import os
import random

import telegram 
from dotenv import load_dotenv

from save_image import NAME_FOLDER



def send_image(name_image, chat_id, bot):
    with open(os.path.join(NAME_FOLDER, f"{name_image}"), "rb") as image:
        bot.send_document(chat_id=chat_id, document=image)

def random_image():
    images = os.listdir(NAME_FOLDER)
    return random.choice(images)

if __name__ == "__main__":
    load_dotenv()
    api_bot = os.getenv("API_BOT")
    chat_id = os.getenv("CHAT_ID")
    name_image = random_image() 
    bot = telegram.Bot(token=api_bot)
    send_image(name_image, chat_id)
   