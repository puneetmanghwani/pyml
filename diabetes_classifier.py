#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("pima-indians-diabetes-deepnet.csv")


# In[13]:


df.head(15)


# In[14]:


df.columns


# In[10]:


from sklearn.tree import DecisionTreeClassifier


# In[11]:


algo_DT=DecisionTreeClassifier()


# In[12]:


from sklearn.model_selection import train_test_split


# In[15]:


x_train,x_test,y_train,y_test=train_test_split(df[['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']],df['diabetes'],test_size=0.1)


# In[16]:


train_DT=algo_DT.fit(x_train,y_train)


# In[17]:


prediction_DT=algo_DT.predict(x_test)


# In[44]:


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


# 
# print('accuracy is ->',accuracy_score(y_test,prediction_DT))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_DT))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_DT))
# 

# In[20]:


from sklearn.ensemble import RandomForestClassifier


# In[21]:


algo_RF=RandomForestClassifier(n_estimators=100)


# In[27]:


train_RF=algo_RF.fit(x_train,y_train)


# In[28]:


prediction_RF=train_RF.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_RF))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_RF))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_RF))
# 

# In[30]:


from sklearn.svm import SVC


# In[31]:


algo_SVM=SVC()


# In[32]:


train_SVM=algo_SVM.fit(x_train,y_train)


# In[33]:


prediction_SVM=algo_SVM.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_SVM))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_SVM))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_SVM))
# 

# In[35]:


param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']} 


# In[36]:


from sklearn.model_selection import GridSearchCV


# In[37]:


algo_GR_SVM= GridSearchCV(SVC(),param_grid,refit=True,verbose=3)


# In[38]:


train_GR_SVM=algo_GR_SVM.fit(x_train,y_train)


# In[39]:


prediction_GR_SVM=algo_GR_SVM.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_GR_SVM))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_GR_SVM))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_GR_SVM))
# 

# In[61]:


print('enter your input for diabetes')


# In[173]:


test_data= list(map(float,input('enter the preg,plas,pres,skin,test,mass,pedi and age').split()))


# In[174]:


test_data=pd.DataFrame(data=(np.array(test_data)).reshape((1,8)),columns=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age'])


# In[175]:


prediction_by_DT=algo_DT.predict(test_data)
prediction_by_RF=algo_RF.predict(test_data)
prediction_by_GR_SVM=algo_GR_SVM.predict(test_data)


# In[184]:


avg_prediction=int((prediction_by_DT+prediction_by_RF+prediction_by_GR_SVM)/2)
if(avg_prediction==1):
    print('yes you have diabetes')
else:
    print('no you don\'t have diabetes')


# In[ ]:




