import fake_useragent
import requests
import main
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = main.conn('https://24.kg/')
    soup = BeautifulSoup(r, 'html.parser')
    t0 = soup.find_all('div', {'class': 'row lineNews'})
    houp = BeautifulSoup(str(t0), 'html.parser')
    t = houp.find_all('div', {'class': 'one'})
    for i in range(0, 7):
        t1 = str(t[i])
        link = t1[str.find(t1, 'href') + 6:]
        link = 'https://24.kg' + link[:str.find(link, '"')]
        lead_head = t[i].text
        second_head = ''
        time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + lead_head[1:6], "%d_%m_%Y|%H:%M")
        if time_head - timedelta(hours=3) < datetime.today():
            if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=359):
                main.tg_post(lead_head[7:], second_head, link)
except Exception as exx:
    print(exx)
time.sleep(300)