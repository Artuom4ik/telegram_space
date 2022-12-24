import os 
import requests 
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
from urllib.parse import urlparse
import os.path


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


def extensions(links):
    parse = urlparse(links)
    split = os.path.splitext(parse.path)
    return split[1]


def nasa(api_nasa):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_nasa}&count=5"
    response = requests.get(url)
    links = response.json()
    lst = []
    for link_1 in links:
        lst.append(link_1["hdurl"])
    for number, link in enumerate(lst):
        path = f"images/nasa_apod_{number}.jpeg"    
        save_image(link, path)



load_dotenv()
api_nasa = os.getenv('API_NASA')
os.makedirs("images", exist_ok=True)
id_launch = "5eb87d46ffd86e000604b388"
fetch_spacex_launch(id_launch)
nasa(api_nasa)




