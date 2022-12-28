def fetch_epic_image(nasa_token):
    params = {
        "api_key": nasa_token,
    }
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    images_response = response.json()
    for number, image in enumerate(images_response):
        date = datetime.datetime.fromisoformat(image["date"])
        name_image = image["image"]
        url_image = f"https://api.nasa.gov/EPIC/archive/natural/{now.year}/{now.month}/{now.day}/png/{name_image}.png"
        response_image = requests.get(url_image, params=params)
        response_image.raise_for_status()
        path = f"images/epic_image_{number}.png"
        save_image(response_image.url, path)
