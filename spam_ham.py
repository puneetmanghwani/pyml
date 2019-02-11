#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log,sqrt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from wordcloud import WordCloud
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


mails=pd.read_csv('spam.csv',encoding='latin-1')
mails.head()


# In[3]:


mails=mails.drop(labels=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1)
mails.columns=['label','message']
mails=mails[['message','label']]
mails.head()


# In[4]:


def converter(label):
    if label=='ham':
        return 1
    else:
        return 0
    


# In[5]:


mails['label']=mails['label'].apply(converter)


# In[6]:


spam_emails=' '.join(list(mails[mails['label']==0]['message']))
spam_cloud=WordCloud(width=512,height=512).generate(spam_emails)
plt.figure(figsize=(10,10))
plt.imshow(spam_cloud)

plt.axis('off')


# In[7]:


ham_emails=' '.join(list(mails[mails['label']==1]['message']))
ham_cloud=WordCloud(width=512,height=512).generate(ham_emails)
plt.figure(figsize=(10,10))
plt.imshow(ham_cloud)

plt.axis('off')


# In[8]:


def convert_text(message,gram=1):
    message=message.lower()
    words=word_tokenize(message)
    
    words=[w for w in words if len(w)>2]
    
    if gram>1:
        w=[]
        for i in range(len(words)-2+1):
            w+=[' '.join(words[i:i+gram])]
        return w
    sw=stopwords.words('english')
    words=[word for word in words if word not in sw]
    
    stemmer=PorterStemmer()
    words=[stemmer.stem(word) for word in words]
    
    return words


# In[43]:


from sklearn.feature_extraction.text import CountVectorizer


# In[44]:


bow_transformer = CountVectorizer(analyzer=convert_text).fit(mails['message']) 


# In[45]:


messages_bow = bow_transformer.transform(mails['message'])


# In[46]:


print('Shape of Sparse Matrix: ',messages_bow.shape)
print('Amount of non-zero occurences:',messages_bow.nnz)


# In[47]:


sparsity =(100.0 * messages_bow.nnz/(messages_bow.shape[0]*messages_bow.shape[1]))
print('sparsity:{}'.format(round(sparsity)))


# In[48]:


from sklearn.feature_extraction.text import TfidfTransformer


# In[49]:


tfidf_transformer=TfidfTransformer().fit(messages_bow)


# In[50]:


print(tfidf_transformer.idf_[bow_transformer.vocabulary_['so']])



# In[51]:


messages_tfidf=tfidf_transformer.transform(messages_bow)

print(messages_tfidf.shape)


# In[52]:


from sklearn.model_selection import train_test_split


# In[53]:


x_train,x_test,y_train,y_test=train_test_split(messages_tfidf,mails['label'],test_size=0.1)


# In[54]:


from sklearn.naive_bayes import MultinomialNB


# In[55]:


algo=MultinomialNB()


# In[56]:


train=algo.fit(x_train,y_train)


# In[57]:


test=algo.predict(x_test)


# In[58]:


from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score


# In[59]:


print(classification_report(test,y_test))
print(confusion_matrix(test,y_test))
print(precision_score(test,y_test))


# In[60]:


test1=algo.predict(messages_tfidf1)
test2=algo.predict(messages_tfidf2)
test9=algo.predict(messages_tfidf9)
test10=algo.predict(messages_tfidf10)


# In[ ]:




