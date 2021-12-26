#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Create DataFrame
a = [[1, 231, 'Self-employed', 9, 'High', 2, 30200],

[2, 765, 'students', 5, 'high', 3, 12700],

[3, 453, 'Horeca', 7, 'medium', 5, 89400],

[4, 231, 'self-employed', 9, 'high', 2, 30200],

[5, 892, 'finance', 3, 'low', 3, 740000]]




df =pd.DataFrame(a,
                
                columns = ['TransactionID', 'ClientID', 'Profession', 'Bank_dep', 'Risk', 'Number of credits', 'Revenue']
                )

df


# In[4]:


from sklearn.preprocessing import OneHotEncoder

x = [[11,"Spain"], [22,"France"],[33,"Spain"],[44,"Germany"]]
y = OneHotEncoder().fit_transform(x).toarray()

print(y)
df


# In[7]:


y = pd.get_dummies(df.Revenue, prefix = 'Risk') #create a dummie DF 
print(y.head())

