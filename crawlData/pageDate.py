import requests
from bs4 import BeautifulSoup
from http.client import responses
from lxml import etree

salary_xpath = '/html/body/div/div[3]/div[1]/div/div[1]/section/ul[1]/li[5]/div/span'
payload = {
    'o-flyForm__textInput': '===',
    '#password': '====='
}
def pageData(url, selector, selector_type) -> dict:
    with requests.Session() as s:
        p = s.post('https://jobinja.ir/login/user', data=payload)
        print(p.text)
        print(responses[p.status_code])
    # selector and selector_type will be added soon
        data = {}
        page = s.get(url, auth=(user, password)) 
        if responses[page.status_code] == 'OK':
            try:
                soup = BeautifulSoup(page.content, 'html.parser')
                html = etree.HTML(str(soup))
                data['title'] = soup.find(class_='c-jobView__titleText').text.replace('\n', '').replace('استخدام', '').strip()
                salary = html.xpath(salary_xpath)
                data['salary'] = html.xpath(salary_xpath)
                print(data)
            except:
                raise Exception('something is wrong!!!')
        else:
            raise Exception(f"oos, we have an error: {responses[page.status_code]}")
    

pageData('https://jobinja.ir/companies/khedmatazma-1/jobs/CNph/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-data-analyst-%D8%AF%D8%B1-%D8%AE%D8%AF%D9%85%D8%AA-%D8%A7%D8%B2-%D9%85%D8%A7?_ref=16','','')
