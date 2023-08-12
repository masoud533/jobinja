import requests
from bs4 import BeautifulSoup
from http.client import responses


def ads(url, selector, selector_type):
    # selector and selector_type will be added soon
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        dic = {}
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all(class_='c-jobListView__titleLink')
        for link in links:
            dic[(link.text).replace(" ", "").replace('\n', '')] = link.get('href')
        print(dic)
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")
    

ads('https://jobinja.ir/jobs?&filters%5Bjob_categories%5D%5B%5D=&filters%5Bkeywords%5D%5B0%5D=data&filters%5Blocations%5D%5B%5D=&preferred_before=1691678646&sort_by=relevance_desc', '', '')
