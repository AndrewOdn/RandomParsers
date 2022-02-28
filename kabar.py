import fake_useragent
import requests
import tools
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = tools.conn('https://kabar.kg/')
    soup = BeautifulSoup(r, 'html.parser')
    to = soup.find_all('div', {'class': 'col-md-12'})
    houp = BeautifulSoup(r, 'html.parser')
    t0 = soup.find_all('article')
    for i in range(0, 4):
        t = str(t0[i])
        link = t[str.find(t, 'href') + 6:]
        link = 'https://kabar.kg' + link[:str.find(link, '"')]
        lead_head = t0[i].text
        time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + lead_head[3:8], "%d_%m_%Y|%H:%M")
        if time_head - timedelta(hours=3) < datetime.today():
            if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=3590):
                second_head = ''
                pic = ''
                try:
                    r = tools.conn(link)
                    loup = BeautifulSoup(r, 'html.parser')
                    x1 = loup.find('meta', {'property': 'og:image'})
                    pigs = str(x1)
                    pic = pigs[str.find(pigs, 'content') + 9:]
                    pic = pic[:str.find(pic, '"')]
                    if str.find(pic, 'https:') == -1:
                        pic = 'https:' + pic
                    x2 = loup.find('p', {'style': 'text-align: justify;'})
                    if x2 is None:
                        x2 = loup.find('p', {'style': 'text-align:justify'})
                    pigs = str(x2)
                    second_head = pigs[str.find(pigs, '</strong>') + 9:]
                    second_head = second_head[str.find(second_head, '"')+1:]
                    second_head = second_head[:str.find(second_head, '"')]
                    if str.find(pic, 'https:') == -1:
                        pic = 'https:' + pic
                except Exception as exx:
                    pic = 'img//kabar-logo.gif'
                    print(exx)
                tools.tg_post(lead_head[10:], second_head, link)
                print(pic)
except Exception as exx:
    print(exx)
