#!/usr/bin/env python
# coding: utf-8

# # Plotting Multiple Data Series
# 
# Complete the following set of exercises to solidify your knowledge of plotting multiple data series with pandas, matplotlib, and seaborn. Part of the challenge that comes with plotting multiple data series is transforming the data into the form needed to visualize it like you want. For some of the exercises in this lab, you will need to transform the data into the form most appropriate for generating the visualization and then create the plot.

# In[1]:


#warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


# In[2]:


data = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Lab 2\liquor_store_sales.csv')
data.head()
data.shape # to heavy so need to create a new DF that we are going to sort out


# In[3]:


data.head()


# In[4]:


data1= data.groupby("ItemType").agg("sum")


# In[5]:


data1


# In[6]:


data1.shape


# In[7]:


# Let`s drop 2 columns: year and month
data1.drop(['Year','Month'],axis=1, inplace=True)


# In[8]:


data1


#  ## 1. Create a bar chart with bars for total Retail Sales, Retail Transfers, and Warehouse Sales by Item Type.

# In[9]:


# 1st method

data1.plot(kind = 'bar')


# In[10]:


#2nd method
data1.plot.bar()


# In[11]:


data1.plot.barh()


# ## 2. Create a horizontal bar chart showing sales mix for the top 10 suppliers with the most total sales. 

# In[12]:


data2 = data.groupby("Supplier").agg("sum")


# In[13]:


data2


# In[14]:


#Add a new column then cocatenate 3 columns
data2['Salesmix'] = (data2['RetailSales']+data2['RetailTransfers']+data2['WarehouseSales'])


# In[15]:


data2


# In[16]:


#drop columns Year, Month, Retail Sales, Retail, warehouse
data2.drop(['Year','Month','RetailSales','RetailTransfers','WarehouseSales'],axis=1, inplace=True)


# In[17]:


data2


# In[18]:


#we sort ou the column
top_lst = data2.sort_values(by=['Salesmix'])


# In[19]:


top_lst


# In[20]:


top_lst = top_lst.head(10)


# In[21]:


top_lst


# In[22]:


top_lst.plot.barh()


# ## 3. Create a multi-line chart that shows average Retail Sales, Retail Transfers, and Warehouse Sales per month over time.

# In[46]:


data3 = data.groupby(["Year","Month"]).agg("mean")


# In[47]:


data3


# In[48]:


data3.sort_values(by=["Year","Month","RetailSales", "RetailTransfers","WarehouseSales"], inplace=True) 


# In[49]:


data3


# In[50]:


data3.plot(x="Month", y =["RetailSales", "RetailTransfers","WarehouseSales"])


# ## 4. Plot the same information as above but as a bar chart.

# In[51]:


data3.plot.bar()


# ## 5. Create a multi-line chart that shows Retail Sales summed by Item Type over time (Year & Month).
# 
# *Hint: There should be a line representing each Item Type.*

# In[52]:


data5 = data1.agg("mean")


# In[53]:


data5


# In[45]:


#Drop columns RetailTransfers and WarehouseSales
data5.drop(['RetailTransfers','WarehouseSales'],axis=1, inplace=True)


# In[54]:


data5


# In[55]:


data5.plot(x='ItemType', y =['Year', 'Month', 'RetailSales'])


# ## 6. Plot the same information as above but as a bar chart.

# In[56]:


data5.plot.bar()


# In[58]:


data5.plot(kind = 'bar')


# ## 7. Create a scatter plot showing the relationship between Retail Sales (x-axis) and Retail Transfers (y-axis) with the plot points color-coded according to their Item Type.
# 
# *Hint: Seaborn's lmplot is the easiest way to generate the scatter plot.*

# In[59]:


data.plot.scatter(x="RetailSales", y =["RetailTransfers"]) #just 1 variable
#plot is the wrapper of matplotlib in Pandas


# ## 8. Create a scatter matrix using all the numeric fields in the data set with the plot points color-coded by Item Type.
# 
# *Hint: Seaborn's pairplot may be your best option here.*

# In[60]:


pd.plotting.scatter_matrix(data)

