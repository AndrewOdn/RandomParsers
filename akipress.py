import fake_useragent
import requests
import main
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = main.conn('https://akipress.org/')
    soup = BeautifulSoup(r, 'html.parser')
    t0 = soup.find('table', {'id': 'maintbl'})
    houp = BeautifulSoup(str(t0), 'html.parser')
    t = houp.find_all('td', {'class':'datetxt'})
    t1 = houp.find_all('a', {'class':'newslink'})
    for i in range(1, 20):
        if i%2 == 1:
            t2 = str(t1[i])
            s = t[i].text
            s = s[1:6]
            link = t2[str.find(t2, 'href') + 7:]
            if str.find(link, 'akipress.org') == -1:
                link = 'https://akipress.org' + link[:str.find(link, '"')]
            else:
                link = 'https:/'+link[:str.find(link, '"')]
            lead_head = t1[i].text
            second_head = ''
            time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + s,
                                          "%d_%m_%Y|%H:%M")
            if time_head - timedelta(hours=3) < datetime.today():
                if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=359):
                    main.tg_post(lead_head[1:], second_head, link)
except Exception as exx:
    print(exx)