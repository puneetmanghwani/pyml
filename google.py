#!/usr/bin/python3

#import urllib2
from googlesearch import search

#parameters 
#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)

data=search('hello',num=10,tld="co.in",stop=10)
print (type(data))
for i in data:
	print(i)
	#link=urllib2.urlopen(i)
	#print(link.read())
