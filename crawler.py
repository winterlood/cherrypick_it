import requests
from bs4 import BeautifulSoup
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('뉴스기사크롤러 시작')

req = requests.get('https://www.yna.co.kr/safe/news')
req.encoding= None
html = req.content
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    'div.contents > div.content01 > div > ul > li >article > div >h3'
    )

data = {}

for title in datas:   
    name = title.find_all('a')[0].text
    url = 'http:'+title.find('a')['href']
    data[name] = url

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii = False, indent='\t')

print('뉴스기사크롤러 끝')