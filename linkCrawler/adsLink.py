import requests
from bs4 import BeautifulSoup
from http.client import responses


def ads(url, selector, selector_type) -> dict:
    # selector and selector_type will be added soon
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        try:
            dic = {}
            soup = BeautifulSoup(page.content, 'html.parser')
            links = soup.find_all(class_='c-jobListView__titleLink')
            for link in links:
                dic[(link.text).replace(" ", "").replace('\n', '')] = link.get('href')
            return dic
        except:
            raise Exception('something is wrong!!!')
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")