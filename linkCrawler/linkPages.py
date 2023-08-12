import requests
from bs4 import BeautifulSoup
from http.client import responses

def pages(url: str, selector: str, selector_type: str):
    page = responses.get(url)
    if responses[page.status_code] == 'ok':
        pass
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")