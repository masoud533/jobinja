import requests
from bs4 import BeautifulSoup
from http.client import responses

def pages(url: str, selector: str, selector_type: str) -> list:
    # selector and selector_type will be added soon
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            links = soup.find(class_='paginator').find_all('a')
        except:
            raise Exception("something is wrong!!!")
        links = [x.get('href') for x in links]
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")
    
