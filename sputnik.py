import re

import fake_useragent
import requests
import tools
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = tools.conn('https://ru.sputnik.kg/news/')
    soup = BeautifulSoup(r, 'html.parser')
    t0 = soup.find('div', {'class': 'list list-tag'})
    houp = BeautifulSoup(str(t0), 'html.parser')
    names = houp.find_all('a', {'class':'list__title'})
    pics = houp.find_all('div', {'class':'list__image'})
    date = houp.find_all('div', {'class':'list__date'})
    for i in range(0, len(names)):
        ll = str(names[i])
        pigs = str(pics[i])
        link = ll[str.find(ll, 'href') + 7:]
        if requests.get('https://ru.sputnik.kg/' + link[:str.find(link, '"')]).status_code != 404:
            link = 'https://ru.sputnik.kg/' + link[:str.find(link, '"')]
        else:
            if requests.get('https:/'+link[:str.find(link, '"')]).status_code != 404:
                link = 'https:/'+link[:str.find(link, '"')]
            else:
                link = link[:str.find(link, '"')]
        lead_head = names[i].text
        pic = pigs[str.find(str(pics[i]), 'src') + 8:]
        pic = pic[:str.find(pic, '"')]
        try:
            time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + date[i].text,
                                      "%d_%m_%Y|%H:%M")
        except:
            aa = date[i].text
            time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + aa[7:],
                                          "%d_%m_%Y|%H:%M")
        if time_head - timedelta(hours=3) < datetime.today():
            if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=359):
                try:
                    r1 = tools.conn(link)
                    foup = BeautifulSoup(r1, 'html.parser')
                    second_head = foup.find('div', {'class': 'article__announce-text'}).text
                except:
                    second_head = ''
                tools.tg_post(lead_head, second_head, link)
                print(pic)
except Exception as exx:
    print(exx)