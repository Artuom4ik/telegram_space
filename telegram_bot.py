import os
import random
import time
import argparse

import telegram
from dotenv import load_dotenv

from send_image import send_image, random_image
from save_image import NAME_FOLDER 


def telegram_bot(chat_id, api_bot):
    bot = telegram.Bot(token=api_bot)
    bot.send_document(chat_id=chat_id, document=image)


def send_random_images(chat_id, bot, time_sleep):
    while True:
        images = os.listdir(NAME_FOLDER)
        random.shuffle(images)
        for image in images:
            send_image(image, chat_id, bot)
            time.sleep(time_sleep)
            
    
def get_time_sleep():
    parser = argparse.ArgumentParser(
        description="""
        Задает время отправки между фотографиями.
        """
    )
    time_sleep = os.getenv("TIME_SLEEP")
    parser.add_argument("time_sleep", default=time_sleep, type=int, nargs="?")
    args = parser.parse_args()
    return args.time_sleep


if __name__ == "__main__":
    load_dotenv()
    chat_id = os.getenv("CHAT_ID")
    api_bot = os.getenv("API_BOT")
    bot = telegram.Bot(token=api_bot)    
    time_sleep = get_time_sleep()
    send_random_images(chat_id, bot, time_sleep)
