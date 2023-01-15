import os.path
import os

import requests

from urllib.parse import urlparse


NAME_FOLDER = "images"


def create_folder(NAME_FOLDER):
    os.makedirs(NAME_FOLDER, exist_ok=True)


def save_image(link, path):
    response = requests.get(link)
    response.raise_for_status()
    with open(path, "wb") as image:
        image.write(response.content)


def get_extensions(link):
    path_image = urlparse(link).path
    extensions_image = os.path.splitext(path_image)[1]
    return extensions_image
