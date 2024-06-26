import os
import argparse

import requests
from dotenv import load_dotenv

from save_image import save_image, create_folder, NAME_FOLDER


def fetch_spacex_launch(id_launch):
    url = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(url)
    links = response.json()["links"]["flickr"]["original"]

    if links:
        for number, link in enumerate(links):
            path = os.path.join(NAME_FOLDER, f"spacex_{number}.jpeg")
            save_image(link, path)
    
    else:
        print('Изображения не найдены')


def get_id():
    parser = argparse.ArgumentParser(
        description="""
        Скачивает фотографии SpaceX запуска ракет, по указанному id запуска.
        """
    )
    parser.add_argument("id_launch", type=str, nargs="?")
    args = parser.parse_args()
    return args.id_launch


if __name__ == "__main__":
    load_dotenv()
    create_folder(NAME_FOLDER)
    fetch_spacex_launch(get_id())
