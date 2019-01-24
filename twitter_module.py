#!/usr/bin/python3
import tweepy
import cursor
import matplotlib.pyplot as plt
import re
from  nltk.tokenize  import  sent_tokenize
from  nltk.tokenize  import  word_tokenize
from  nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from  textblob  import TextBlob

consumer_key="bSh5wvnGDnoE0HShQjbLcDCj5"
consumer_secret="mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
access_key="2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
access_secret="BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff"


def get_tweets_handler(): 
        username=input('enter the twitter handler name')
                 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
 
        auth.set_access_token(access_key, access_secret) 
       
        api = tweepy.API(auth) 
    
        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username) 
  
        data=""	
      
        tweets_for_csv = [tweet.text for tweet in tweets]  
        for j in tweets_for_csv: 
           
            data=data+j
        
        tweets_editing(data)
        
        frequency_distribution = nltk.FreqDist(data)
        count=frequency_distribution.most_common(20)
        x=[]
        y=[]
        for freq in count:
                x.append(freq[0])
                y.append(freq[1])

        plt.plot(x,y)
        plt.show()


def get_tweets_topic():
    data=""	

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_key, access_secret) 

    api = tweepy.API(auth)	

    topic=tweepy.Cursor(api.search,input('enter any topic or  hashtag to be searched'))

    for items in topic.items(50):
        data=data+items.text

    tweets_editing(data)

        
def tweets_editing(data):
        data=re.sub('http\S+'," ",data)
        data=re.sub('@\S+'," ",data)
        data=re.sub('#\S+'," ",data)
        sent_token=sent_tokenize(data)
        
        lemma=WordNetLemmatizer()
        main_data=""

        for  i  in  range(len(sent_token)):
            words=word_tokenize(sent_token[i])
            newword=[lemma.lemmatize(word) for word in words]
            data1=" ".join(newword)
            main_data=main_data+data1
        
        f=open('/home/punit/twitter_scraped.txt','w')
        f.write(main_data)
        f.close()

        analysis(data)	  
          
          

def analysis(data):	
	analyse=TextBlob(data)
	check=analyse.sentiment
	print(check)
	




