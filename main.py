from bs4 import BeautifulSoup
import requests
from flask import Flask
from json2html import *


def parse():
    headers = {
        'authority': 'world-weather.ru',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'service-worker-navigation-preload': 'true',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'showBlocks=all%2C1%2C1%2C1%2C1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; _ga=GA1.2.402370250.1619434472; _gid=GA1.2.605756376.1619434472; _ym_uid=1619434472547185874; _ym_d=1619434472; __gads=ID=0a05119252749708-2244f185f1c700da:T=1619434471:RT=16194344 71:S=ALNI_MbjzRiSxwTFaaQlaI23M93lPjHXow; _ym_isad=2',
    }

    response = requests.get('https://world-weather.ru/pogoda/kazakhstan/astana/june-2021/', headers=headers)

    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup)
    days = soup.find_all(class_='ww-month-weekdays')
    all_days = []
    dct = []
    d = dict()

    for day in days:
        d['day'] = int(day.contents[0].contents[0])
        d['description'] = day.contents[1]['title']
        d['temperature'] = day.contents[2].text
        dct.append(d.copy())

    response = dict()
    response['all_days'] = all_days
    return json2html.convert(json = dct)

app = Flask(__name__)

@app.route('/almaty/june-2021')
def hello_world():
    print(parse())
    return parse()

if __name__ == '__main__':
    app.run()





