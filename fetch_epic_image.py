import os
import datetime
import argparse

import requests
from dotenv import load_dotenv

from save_image import save_image, NAME_FOLDER, create_folder


def fetch_epic_image(nasa_token, count):
    params = {
        "api_key": nasa_token
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()[:count]
    for number, image in enumerate(images_response):
        date = datetime.datetime.fromisoformat(image["date"])
        image_date = date.strftime("%Y/%m/%d")
        name_image = image["image"]
        url_image = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{name_image}.png"
        response_image = requests.get(url_image, params=params)
        response_image.raise_for_status()
        path = os.path.join(NAME_FOLDER, f"epic_image_{number}.png")
        save_image(response_image.url, path)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.getenv("API_NASA")
    parser = argparse.ArgumentParser(
        description="""
        Скачивает фотографии Земли.
        """
    )
    parser.add_argument("count", default=10, type=int, nargs="?")
    args = parser.parse_args()
    count = args.count
    create_folder(NAME_FOLDER)
    fetch_epic_image(nasa_token, count)
