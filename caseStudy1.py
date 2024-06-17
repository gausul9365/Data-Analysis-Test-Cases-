#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Ecommerce Purchases")


# In[3]:


data


# In[ ]:





# In[4]:


data.head()


# data.head(10)

# In[78]:


**Check Last 10 Rows of The Dataset**


# In[6]:


data.tail(10)


# In[7]:


data.dtypes


# In[8]:


data


# In[9]:


data.isnull


# In[ ]:





# In[10]:


data.isnull().sum()


# In[11]:


data


# In[ ]:





# In[12]:


data.columns


# In[ ]:





# In[14]:


len(data.columns)


# In[16]:


data.info()


# In[17]:


data.columns


# **How many rows and columns are there in our Dataset?**

# In[18]:


data['Purchase Price'].max


# **Highest and Lowest  and mean Purchase Prices**

# In[19]:


data['Purchase Price'].max()


# In[ ]:





# In[20]:


data['Purchase Price'].min()


# In[ ]:





# In[21]:


data['Purchase Price'].mean()


# In[ ]:





# In[25]:


data.columns


# **How many people have French 'fr' as their Language?**

# In[26]:


data['Language']


# In[ ]:





# In[27]:


data['Language']=='fr'


# In[ ]:





# In[29]:


data[data['Language']=='fr']


# In[ ]:





# In[30]:


len(data[data['Language']=='fr'])


# In[31]:


data[data['Language']=='fr'].count()


# In[32]:


data.columns


# **Job Title Contains Engineer**

# In[33]:


data['Job']


# In[38]:


data[data['Job'].str.contains('engineer',case= False)]


# In[ ]:





# In[39]:


len(data[data['Job'].str.contains('engineer',case= False)])


# In[40]:


data[data['Job'].str.contains('engineer',case= False)].count()


# In[41]:


data.columns


# **Find The Email of the person with the following IP Address: 132.207.160.22**

# In[43]:


data[data['IP Address']=="132.207.160.22"]


# In[ ]:





# In[44]:


data[data['IP Address']=="132.207.160.22"]['Email']


# In[45]:


data.columns


# **How many People have Mastercard as their Credit Card Provider and made a purchase above 50?**

# In[46]:


data['CC Provider']=="Mastercard"


# In[ ]:





# In[47]:


(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)


# In[ ]:





# In[48]:


data[(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)]


# In[49]:


len(data[(data['CC Provider']=="Mastercard") & (data['Purchase Price']>50)])


# In[50]:


data.columns


# **Find the email of the person with the following Credit Card Number: 4664825258997302**

# In[57]:


data[data['Credit Card']==4664825258997302]['Email']


# **How many people purchase during the AM and how many people purchase during PM?**

# In[58]:


data['AM or PM']


# In[ ]:





# In[59]:


data['AM or PM'].value_counts()


# In[60]:


data.columns


# **How many people have a credit card that expires in 2020?**

# In[61]:


data['CC Exp Date']


# In[62]:


def fun() :
    count = 0
    for date in data ['CC Exp Date']:
        if date.split('/')[1]=='20':
            count = count+1
    print (count)


# In[63]:


fun()


# In[ ]:


#another method


# In[64]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')])


# In[69]:


list1 = []
for email in data['Email']:
    list1.append(email.split('@')[1])


# In[71]:


data['temp']=list1


# In[72]:


data.head()


# In[73]:


data['temp'].value_counts().head()


# **What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)**

# In[75]:


data['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()


# In[ ]:




