import re

import fake_useragent
import requests
import tools
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
try:
    r = tools.conn('https://akipress.org/')
    soup = BeautifulSoup(r, 'html.parser')
    t0 = soup.find('table', {'class': 'sections section-last'})
    houp = BeautifulSoup(str(t0), 'html.parser')
    t = houp.find_all('td', {'class':'datetxt'})
    t1 = houp.find_all('a', {'class':'newslink'})
    for j in range(0, 20):
        l1 = t[j].text
        l1= ' '.join(l1.split())
        if l1 != '':
            t2 = str(t1[j])
            s = t[j].text
            s = s[1:6]
            link = t2[str.find(t2, 'href') + 7:]
            if requests.get('https://akipress.org' + link[:str.find(link, '"')]).status_code != 404:
                link = 'https://akipress.org' + link[:str.find(link, '"')]
            else:
                if requests.get('https:/'+link[:str.find(link, '"')]).status_code != 404:
                    link = 'https:/'+link[:str.find(link, '"')]
                else:
                    link = link[:str.find(link, '"')]
            lead_head = t1[j].text

            time_head = datetime.strptime(datetime.today().strftime('%d_%m_%Y') + '|' + s,
                                          "%d_%m_%Y|%H:%M")
            if time_head - timedelta(hours=3) < datetime.today():
                if time_head - timedelta(hours=3) > datetime.today() - timedelta(seconds=359):
                    pic = ''
                    second_head = ''
                    try:
                        r = tools.conn(link)
                        loup = BeautifulSoup(r, 'html.parser')
                        x1 = loup.find('meta', {'property':'og:image'})
                        pigs = str(x1)
                        pic = pigs[str.find(pigs, 'content') + 9:]
                        pic = pic[:str.find(pic, '"')]
                        if str.find(pic, 'https:') == -1:
                            pic = 'https:' + pic
                        x2 = loup.find('meta', {'property': 'og:description'})
                        pigs = str(x2)
                        second_head = pigs[str.find(pigs, 'content') + 9:]
                        second_head = second_head[:str.find(second_head, '"')]
                        if str.find(pic, 'https:') == -1:
                            pic = 'https:' + pic
                    except Exception as exx:
                        pic = 'img//akipress_logo.png'
                        print(exx)
                    tools.tg_post(lead_head, second_head, link)
                    print(pic)
except Exception as exx:
    print(exx)