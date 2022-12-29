import os.path

from urllib.parse import urlparse


def get_extensions(link):
    path_image = urlparse(link).path
    extensions_image = os.path.splitext(path_image)[1]
    return extensions_image
