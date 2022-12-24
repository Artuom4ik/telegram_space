import os 
import requests 
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv


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


os.makedirs("images", exist_ok=True)
id_launch = "5eb87d46ffd86e000604b388"
fetch_spacex_launch(id_launch)





