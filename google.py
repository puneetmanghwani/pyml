#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from googlesearch import search

data=search('hello',num=5,tld="co.in",stop=5)
print (type(data))
for i in data:
    source = requests.get(i).text
    soup = BeautifulSoup(source, 'lxml')
    for p in soup.select('p'):
        print(p.text)
    print('___----____--%^%&^@!%$&^%$(!%$&^#@%$*&!+_____------_____#@^*&^$*&@#')

	
	
