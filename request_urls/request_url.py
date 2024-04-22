import json
import requests


def json_load():
    with open("request_urls/urls.json", "r") as f:
        urls = json.load(f)
        return urls


url = json_load()


def request_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    raise Exception("Failed to fetch web page. Status code:", response.status_code)
