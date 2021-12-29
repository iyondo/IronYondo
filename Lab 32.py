#!/usr/bin/env python
# coding: utf-8
Method:
1 - Check the columns with missing values
2 - Replace this missing values by 0
3 - Check if there is any duplicate
4 - Check the total amount per client
5 - Encoding with Get Dummies - Profession
6 - Encoding with LabelBinazer - BirthYear
# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# import data set 
data =pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 32\example_data_cleaning.xlsx - Sheet1.csv')
data


# In[3]:


# sum method to total up the number of True values(missing values) by column
null_cols = data.isnull().sum() #isnull - check whether the value in each field is missing (null) and return True or False
null_cols[null_cols > 0]



# In[4]:


data['BirthYear'].dtype


# In[5]:


data['Profession'].dtype


# In[6]:


# looks like the BirtYear column and the Profession column have a similar number of nulls
# Perhaps it`s the same persons
# Investigation by subsetting the data set and looking at just the records where BirtYear is null and just the columns we think will be informative in allowing us to determine a reason


null_displ = data[(data['BirthYear'].isnull()==True)]
null_displ = null_displ[['TransactionID', 'ClientID', 'BirthYear', 'Amount', 'Profession','Department', 'Risk']]
null_displ


# In[7]:


# Investigation by subsetting the data set and looking at just the records where Profession is null and just the columns we think will be informative in allowing us to determine a reason

null_displ = data[(data['Profession'].isnull()==True)]
null_displ = null_displ[['TransactionID', 'ClientID', 'BirthYear', 'Amount', 'Profession','Department', 'Risk']]
null_displ


# Not a duplicate for clientID|35008 - 2 different transactions


# In[8]:


# Finding and Removing Duplicates: the drop_duplicates method. 
# We use the len method to calculate the number of rows in the data set both before and after removing duplicates 
# Then print the number of rows dropped
before = len(data)
data = data.drop_duplicates()
after = len(data)
print('Number of duplicate records dropped: ', str(before - after))

# there were no records that matched exactly across all columns.


# In[9]:


# Imputation using (Zero/Constant) Values:
data = data.fillna(0)
data


# In[10]:


# We notice that in some cases the first letter is not a capital letter or there is mistake in the spelling 
# We can make that more consistent by using the same technique. 
data['Profession'] = data['Profession'].str.replace('hr', 'HR')
data['Profession'] = data['Profession'].str.replace('student', 'Student')
data['Profession'] = data['Profession'].str.replace('barmen', 'Barmen')
data['Profession'] = data['Profession'].str.replace('manager', 'Manager')
data['Profession'] = data['Profession'].str.replace('sailer', 'Sailer')
data['Profession'] = data['Profession'].str.replace('bdm', 'BDM')
data['Profession'] = data['Profession'].str.replace('researcher', 'Researcher')
data['Profession'] = data['Profession'].str.replace('professor', 'Professor')
data['Profession'] = data['Profession'].str.replace('developer', 'Developer')
data['Profession'] = data['Profession'].str.replace('etudient', 'Student')


print(set(data['Profession']))


# In[11]:


data


# In[12]:


# Total amount per client
data1 = data.groupby('ClientID').agg({'Amount': 'sum'})
data1


# In[13]:


# Encoding: 1st method - Get Dummies on column Profession,
y = pd.get_dummies(data.Profession, prefix = 'Profession') #create a dummie DF using df countries, with prefix Country
print(y.head())


# In[14]:


#2nd method - on column BirthYear

from sklearn.preprocessing import LabelBinarizer #import method
y = LabelBinarizer().fit_transform(data.BirthYear) #initialization of method
y

