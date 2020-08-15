#!/usr/bin/env python3
# Anchor extraction from HTML document

#Crawling way_1
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('https://www.naver.com/') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.select("span.keyword"):
#         print(anchor.get_text())

#Crawling way_2
import requests
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('span.item_title')
i=1
for item in data:
    print(str(i)+"위: "+item.get_text())
    i+=1
i=1
sys.stdout = open("Result_crawling.txt","w")
for item in data:
    print(str(i)+"위: "+item.get_text())
    i+=1
sys.stdout.close()



