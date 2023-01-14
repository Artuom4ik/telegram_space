import os
import random

import telegram 
from dotenv import load_dotenv



def send_image(name_image, chat_id, bot):
    with open(os.path.join("images", f"{name_image}"), "rb") as image:
        bot.send_document(chat_id=chat_id, document=image)

def random_image():
    dirs = os.listdir("images")
    return random.choice(dirs)

if __name__ == "__main__":
    load_dotenv()
    api_bot = os.getenv("API_BOT")
    chat_id = os.getenv("CHAT_ID")
    name_image = random_image() 
    bot = telegram.Bot(token=api_bot)
    send_image(name_image, chat_id)
   