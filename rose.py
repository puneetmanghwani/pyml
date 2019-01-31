#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import csv
import nltk

source = requests.get('http://en.wikipedia.org/wiki/Rose').text

soup = BeautifulSoup(source, 'lxml')

#csv_file = open('cms_scrape.csv', 'w')

#csv_writer = csv.writer(csv_file)
#csv_writer.writerow(['headline', 'summary', 'video_link'])
data=""
for p in soup.select('p'):
  data=data+p.text
  if len(data.split())>300:
     break
  
print(data)  

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

sent_token = sent_tokenize(data)
word_token = word_tokenize(data)

#print(sent_token)

#print("_______________&**************(^&*!^(*!&(*@!&#!@*#(@!&#()@!&#(*&@!#(@!________________")

#print(word_token)



