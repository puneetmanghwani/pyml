#!/usr/bin/python3
import tweepy
import cursor
import nltk
import matplotlib.pyplot as plt
from nltk.stem import PorterStemmer

consumer_key="bSh5wvnGDnoE0HShQjbLcDCj5"
consumer_secret="mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"
access_key="2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"
access_secret="BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff"


def get_tweets(username): 
          
       
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
      
        auth.set_access_token(access_key, access_secret) 
  
      
        api = tweepy.API(auth) 
  
  
        number_of_tweets=50
        tweets = api.user_timeline(screen_name=username) 
  
  
        data=""

       # tmp1=tweepy.Cursor(api.search,input('enter any topic hashtag to be searched'))
  	
      
        tweets_for_csv = [tweet.text for tweet in tweets]  
        for j in tweets_for_csv: 
  
           
            data=data+j 
  
        from nltk.tokenize import sent_tokenize
        from nltk.tokenize import word_tokenize

        sent_token = sent_tokenize(data)
        word_token = word_tokenize(data)


        stem_1=PorterStemmer()
        main=""
        for i  in  range(len(sent_token)):
          words=word_tokenize(sent_token[i])
         # print("Stemming----------------------->>")
          newword=[stem_1.stem(word)  for  word  in  words]
         # print(newword)
          data=" ".join(newword)
          #print(data)
          main=main+data
        print(main)
	 
        #   print(sent_token)
        # print('______^&*$%^$%&*#$^&Q($_______')
        # print(word_token)
	
        #text = nltk.Text(word_token)

         #frequency_distribution = nltk.FreqDist(text)
         #print (frequency_distribution.most_common(10))
         #print (frequency_distribution.plot())
         #print(tmp) 
         #for items in tmp1.items(10):
         #  print(items.text)
         #  print('\n')
  	  
# Driver code 
if __name__ == '__main__':
	 
          
      #Here goes the twitter handle for the user 
     # whose tweets are to be extracted. 
     #data=str(input('enter')) 
    # print(input('enter'))
          
    get_tweets(input('enter the username if you want tweets based on it'))
