import os
import argparse

import requests
from dotenv import load_dotenv

from save_image import save_image


def fetch_spacex_launch(id_launch):
    url = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(url)
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate(links):
        path = os.path.join("images", f"spacex_{number}.jpeg")
        save_image(link, path)


def get_id():
    parser = argparse.ArgumentParser(
        description="""
        Скачивает фотографии SpaceX запуска ракет, по указанному id запуска.
        """
    )
    load_dotenv()
    id_launch = os.getenv("ID_LAUNCH")
    parser.add_argument("id_launch", default=id_launch, type=str, nargs="?")
    args = parser.parse_args()
    return args.id_launch


if __name__ == "__main__":
    id_launch = get_id()
    fetch_spacex_launch(id_launch)
