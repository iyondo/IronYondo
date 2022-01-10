#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt   #Seaborn is base on Matpotlib so we still need this library
import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


diamonds = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Projects\Project 4\diamonds_clean.csv')
diamonds.head(10)


# # Pie

# In[10]:


#Group by 'price'
pi = diamonds.groupby(['color'])['price'].mean()
pi


# In[11]:


# Pie - color/price
diamonds.groupby(['color']).sum().plot(kind='pie', y='price', autopct='%1.0f%%', title='Price per color')


# # Boxplot

# In[13]:


#Boxplot for 'y' and 'y' - Outliers
diamonds.boxplot(column=['y','z'], color='black')
plt.title('Outliers for y and z')


# In[14]:


# Seaborn - boxplot: Price per cut
sns.boxplot(data=diamonds, x='cut', y='price').set(title='Price per cut')


# # Subplots

# In[25]:


fig, ax = plt.subplots(1,2, figsize=(10, 5))
sns.boxplot(y=diamonds.y, ax=ax[0])
sns.boxplot(y=diamonds.z, ax=ax[1])
plt.subplots_adjust(wspace=0.5)


# # Bar

# In[15]:


# Seaborn - barplot as horizontal: Price per color
sns.barplot(x = 'price', y = 'color', data = diamonds).set(title='Price per color')


# # Scatterplot

# In[17]:


# Seaborn - Scatter plot - columns 'carat' and 'price'
sns.scatterplot(x="clarity", y="price", hue="price", data=diamonds) 


# In[20]:


diamonds.plot.scatter(x="cut", y =["price"]) #just 1 variable
#plot is the wrapper of matplotlib in Pandas


# In[18]:


#method catplot - looks like frequency
sns.catplot(x="cut", y="price", hue="cut", data=diamonds)


# In[19]:


#method relplot
sns.relplot(x='clarity', y='price', hue="clarity", size="clarity", data=diamonds) 


# # Heatmap

# In[21]:


#Heatmap
plt.figure(figsize=(20, 20))
p = sns.heatmap(diamonds.corr(), annot=True, square=True)


# In[22]:


# Regplot
plt.figure(figsize=(10, 10))
sns.regplot(diamonds.carat, diamonds.price, scatter=True)


# # Scatter Matrix 

# In[23]:


# Scatter Matrix 
pd.plotting.scatter_matrix(diamonds)


# In[28]:


#sort the DF, inplace True to modify the data
diamonds.sort_values(by=["price", "color", "carat", "depth", "clarity"], inplace=True) 

diamonds.plot(x="price", y =["color", "carat", "depth", "clarity"])

