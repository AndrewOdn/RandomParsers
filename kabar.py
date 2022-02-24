import fake_useragent
import requests
import main
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = main.conn('https://kabar.kg/')
    soup = BeautifulSoup(r, 'html.parser')
    to = soup.find_all('div', {'class': 'col-md-12'})
    houp = BeautifulSoup(r, 'html.parser')
    t0 = soup.find_all('article')
    for i in range(0, 4):
        t = str(t0[i])
        link = t[str.find(t, 'href') + 6:]
        link = 'https://kabar.kg' + link[:str.find(link, '"')]
        lead_head = t0[i].text
        second_head = ''
        time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + lead_head[3:8], "%d_%m_%Y|%H:%M")
        if time_head - timedelta(hours=3) < datetime.today():
            if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=359):
                main.tg_post(lead_head[10:], second_head, link)
except Exception as exx:
    print(exx)
