import requests
from bs4 import BeautifulSoup
from http.client import responses


def pageData(url, selector, selector_type) -> dict:
    # selector and selector_type will be added soon
    data = {}
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        pass
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")
