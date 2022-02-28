# This is a sample Python script.
import re
import json
from datetime import datetime, timedelta
import time
import fake_useragent
import requests
from bs4 import BeautifulSoup
import subprocess

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def conn(url):
    try:
        user = fake_useragent.UserAgent().random
        header = {
            'user-agent': user,
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same - origin',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
    except:
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11’',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same - origin',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
    r = requests.Session()
    r = requests.get(url, headers=header)
    return r.text
def tg_post(headline, subline, link):
    post=("<b>"
          +str(headline) #заголовок
          +"</b>\n\n<i>"
          +str(subline) #подзаголовок или первый абзац
          +"</i>\n\n"
          +"<a href=\""
          +link #ссыль
          +"\"><b>Подробности</b> \U0001F447</a>"
         )
    print(post)






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
