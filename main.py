import os
import requests
import os.path

from pprint import pprint
from dotenv import load_dotenv
from urllib.parse import urlparse


def save_image(link, path):
    response = requests.get(link)
    response.raise_for_status()
    with open(path, "wb") as image:
        image.write(response.content)


def fetch_spacex_launch(id_launch):
    url = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(url)
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate(links):
        path = f"images/spacex_{number}.jpeg"
        save_image(link, path)


def get_extensions(link):
    path_image = urlparse(link).path
    extensions_image = os.path.splitext(path_image)[1]
    return extensions_image


def fetch_nasa(nasa_token):
    params = {
        "api_key": nasa_token,
        "count": 30
    }
    url = f"https://api.nasa.gov/planetary/apod"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for number, image in enumerate(images_response):
        link_image = image["url"]
        extension = get_extensions(link_image)
        if image["media_type"] == "image":
            path = f"images/nasa_apod_{number}{extension}"
            save_image(link_image, path)


load_dotenv()
nasa_token = os.getenv('API_NASA')
os.makedirs("images", exist_ok=True)
id_launch = "5eb87d46ffd86e000604b388"
fetch_spacex_launch(id_launch)
fetch_nasa(nasa_token)
