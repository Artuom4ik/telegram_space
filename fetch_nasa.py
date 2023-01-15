import os

import requests
from dotenv import load_dotenv

from save_image import save_image, get_extensions, NAME_FOLDER
from save_image import create_folder


def fetch_nasa(nasa_token):
    params = {
        "api_key": nasa_token,
        "count": 30
    }
    url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for number, image in enumerate(images_response):
        link_image = image["url"]
        extension = get_extensions(link_image)
        if image["media_type"] == "image":
            path = os.path.join(NAME_FOLDER, f"nasa_apod_{number}{extension}")
            save_image(link_image, path)


if __name__ == "__main__":
    load_dotenv()
    create_folder(NAME_FOLDER)
    nasa_token = os.getenv("API_NASA")
    fetch_nasa(nasa_token)
