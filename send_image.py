import os
import random
import argparse

import telegram
from dotenv import load_dotenv

from save_image import NAME_FOLDER


def send_image(name_image, chat_id, bot):
    with open(os.path.join(NAME_FOLDER, f"{name_image}"), "rb") as image:
        bot.send_document(chat_id=chat_id, document=image)


def random_image(image_name):
    if image_name:
        return image_name
    images = os.listdir(NAME_FOLDER)
    return random.choice(images)


def get_name_file():
    parser = argparse.ArgumentParser(
        description="""
        Отправляет фотографию из папки с изображениями.
        """
    )
    parser.add_argument("-n", "--name_image")
    args = parser.parse_args()
    return args.name_image


if __name__ == "__main__":
    load_dotenv()
    api_bot = os.getenv("API_BOT")
    chat_id = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=api_bot)
    name_image = random_image(get_name_file())
    send_image(name_image, chat_id, bot)
