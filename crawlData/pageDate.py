import requests
from bs4 import BeautifulSoup
from http.client import responses
from lxml import etree


def pageData(url, selector, selector_type) -> dict:
    # selector and selector_type will be added soon
    data = {}
    page = requests.get(url)
    if responses[page.status_code] == 'OK':
        try:
            soup = BeautifulSoup(page.content, 'html.parser')
            data['title'] = soup.find(class_='c-jobView__titleText').text.replace('\n', '').replace('استخدام', '').strip()

            print(data)
        except:
            raise Exception('something is wrong!!!')
    else:
        raise Exception(f"oos, we have an error: {responses[page.status_code]}")
    

pageData('https://jobinja.ir/companies/khedmatazma-1/jobs/CNph/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-data-analyst-%D8%AF%D8%B1-%D8%AE%D8%AF%D9%85%D8%AA-%D8%A7%D8%B2-%D9%85%D8%A7?_ref=16','','')
