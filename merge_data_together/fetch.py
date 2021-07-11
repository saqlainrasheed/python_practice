import requests


def get(url):
    response = requests.get(url)
    data = response.json()
    return data
