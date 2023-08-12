import requests
from bs4 import BeautifulSoup
from http.client import responses

def pages(url: str, selector: str, selector_type: str):
    # selector and selector_type will be added soon
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find(class_='paginator').find_all('a')
        print(links)
        links = [x.get('href') for x in links]
        print(links)
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")
    


