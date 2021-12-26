#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Challenge-3" data-toc-modified-id="Challenge-3-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Challenge 3</a></span><ul class="toc-item"><li><span><a href="#Q1:-How-to-identify-VIP-&amp;-Preferred-Customers?" data-toc-modified-id="Q1:-How-to-identify-VIP-&amp;-Preferred-Customers?-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Q1: How to identify VIP &amp; Preferred Customers?</a></span></li><li><span><a href="#How-to-label-customers-whose-aggregated-amount_spent-is-in-a-given-quantile-range?" data-toc-modified-id="How-to-label-customers-whose-aggregated-amount_spent-is-in-a-given-quantile-range?-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>How to label customers whose aggregated <code>amount_spent</code> is in a given quantile range?</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#Sub-Problem-1:-How-to-aggregate-the--amount_spent-for-unique-customers?" data-toc-modified-id="Sub-Problem-1:-How-to-aggregate-the--amount_spent-for-unique-customers?-1.2.0.1"><span class="toc-item-num">1.2.0.1&nbsp;&nbsp;</span>Sub Problem 1: How to aggregate the  <code>amount_spent</code> for unique customers?</a></span></li><li><span><a href="#Sub-Problem-2:-How-to-select-customers-whose-aggregated-amount_spent-is-in-a-given-quantile-range?" data-toc-modified-id="Sub-Problem-2:-How-to-select-customers-whose-aggregated-amount_spent-is-in-a-given-quantile-range?-1.2.0.2"><span class="toc-item-num">1.2.0.2&nbsp;&nbsp;</span>Sub Problem 2: How to select customers whose aggregated <code>amount_spent</code> is in a given quantile range?</a></span></li><li><span><a href="#Sub-Problem-3:-How-to-label-selected-customers-as-&quot;VIP&quot;-or-&quot;Preferred&quot;?" data-toc-modified-id="Sub-Problem-3:-How-to-label-selected-customers-as-&quot;VIP&quot;-or-&quot;Preferred&quot;?-1.2.0.3"><span class="toc-item-num">1.2.0.3&nbsp;&nbsp;</span>Sub Problem 3: How to label selected customers as "VIP" or "Preferred"?</a></span></li></ul></li></ul></li><li><span><a href="#Q2:-How-to-identify-which-country-has-the-most-VIP-Customers?" data-toc-modified-id="Q2:-How-to-identify-which-country-has-the-most-VIP-Customers?-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Q2: How to identify which country has the most VIP Customers?</a></span></li><li><span><a href="#Q3:-How-to-identify-which-country-has-the-most-VIP+Preferred-Customers-combined?" data-toc-modified-id="Q3:-How-to-identify-which-country-has-the-most-VIP+Preferred-Customers-combined?-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Q3: How to identify which country has the most VIP+Preferred Customers combined?</a></span></li></ul></li></ul></div>

# # Challenge 3
# 
# In this challenge we will work on the `Orders` data set. In your work you will apply the thinking process and workflow we showed you in Challenge 2.
# 
# You are serving as a Business Intelligence Analyst at the headquarter of an international fashion goods chain store. Your boss today asked you to do two things for her:
# 
# **First, identify two groups of customers from the data set.** The first group is **VIP Customers** whose **aggregated expenses** at your global chain stores are **above the 95th percentile** (aka. 0.95 quantile). The second group is **Preferred Customers** whose **aggregated expenses** are **between the 75th and 95th percentile**.
# 
# **Second, identify which country has the most of your VIP customers, and which country has the most of your VIP+Preferred Customers combined.**

# ## Q1: How to identify VIP & Preferred Customers?
# 
# We start by importing all the required libraries:

# In[1]:


# import required libraries
import numpy as np
import pandas as pd


# Next, import `Orders` from Ironhack's database into a dataframe variable called `orders`. Print the head of `orders` to overview the data:

# In[2]:


# your code here
Orders=pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 29\Orders.csv')
Orders.head()


# ---
# 
# "Identify VIP and Preferred Customers" is the non-technical goal of your boss. You need to translate that goal into technical languages that data analysts use:
# 
# ## How to label customers whose aggregated `amount_spent` is in a given quantile range?
# 

# We break down the main problem into several sub problems:
# 
# #### Sub Problem 1: How to aggregate the  `amount_spent` for unique customers?
# 
# #### Sub Problem 2: How to select customers whose aggregated `amount_spent` is in a given quantile range?
# 
# #### Sub Problem 3: How to label selected customers as "VIP" or "Preferred"?
# 
# *Note: If you want to break down the main problem in a different way, please feel free to revise the sub problems above.*
# 
# Now in the workspace below, tackle each of the sub problems using the iterative problem solving workflow. Insert cells as necessary to write your codes and explain your steps.

# In[20]:


# your code here 
#Sub Problem 1

Orders1 = Orders.groupby('CustomerID').agg({'amount_spent': 'sum'})
Orders1



# In[ ]:


#Sorting the DataFrame in Ascending Order
#Orders.sort_values(by ='amount_spent') 


# In[7]:



mpg_labels = ['VIP Customers', 'Preferred Customers']

#bins = pd.cut(Orders['amount_spent'],2, labels=mpg_labels) #cut converts to "bins" aka groups of data, here in 2 groups
#bins


# In[13]:


#Create a new colonned binned
Orders['binned'] =  pd.cut(Orders1['amount_spent'], bins = [0.75, 0.95, 100] , labels=mpg_labels)


# In[14]:


Orders['binned'].value_counts()


# In[15]:


Orders


# In[ ]:


data = pd.merge(cars, avg_mpg, on='Make') #merging the two data frames on column 'Make', columns Avg_MPG is at the end
data.head(10)


# Now we'll leave it to you to solve Q2 & Q3, which you can leverage from your solution for Q1:
# 
# ## Q2: How to identify which country has the most VIP Customers?

# In[12]:


# your code here

 Orders1[Orders1['binned']=='VIP Customers'].groupby('Country', as_index=False).agg({'binned': 'count'}) #find de max values (aggregate) for bins1 in DF cars, no index needed


# In[18]:




#df[['col1', 'col2', 'col3', 'col4']].groupby(['col1', 'col2']).agg(['mean', 'count'])
Orders2 = Orders.groupby('CustomerID').agg({'amount_spent', 'Country', 'sum'})
Orders2


# ## Q3: How to identify which country has the most VIP+Preferred Customers combined?

# In[ ]:


# your code here
data1 = Orders.groupby('Country', as_index=False).agg({'binned': 'max'}).max() #find de max values (aggregate) for bins1 in DF cars, no index needed
data1

