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
            path = f"images/nasa_apod_{number}{extension}"
            save_image(link_image, path)