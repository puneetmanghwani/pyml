#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

data=search('hello',num=5,tld="co.in",stop=5)
print (type(data))
main_text=""
for i in data:
    source = requests.get(i).text
    soup = BeautifulSoup(source, 'lxml')
    for p in soup.select('p'):
        main_text=main_text+p.text
#print(main_text)
x=re.sub("Loading...","",main_text)
y=re.sub("Working...","",x)
f=open('/home/punit/scraped.txt','w')
f.write(y)
f.close()
