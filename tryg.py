#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import nltk

inp=input('enter you want to search')
data=search(inp+' wikipedia',num=10,tld="com",stop=10)

for i in data:
	if re.search('wiki',i)!=None:
		print(i)
		break

main_text=""

source = requests.get(i).text
soup = BeautifulSoup(source, 'lxml')
for p in soup.select('p'):
	if(len(main_text.split(' '))>50):
		break
	main_text=main_text+p.text
print(main_text)

