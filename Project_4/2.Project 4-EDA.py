#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics Review
# 
# In this second part of the lab, we are going to continue working with the data that we cleaned in the last part. 
# Be sure to continue to write clean code and comment your work well!
# 
# First, lets import our libraries and the data we saved. 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt   #Seaborn is base on Matpotlib so we still need this library
import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


diamonds = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Projects\Project 4\diamonds_clean.csv')
diamonds.head()


# Now that we cleaned our data, we can proceed with some exploratory analysis. We will analyze the features that affect price the most.
# 
# Let's start by looking at how the charateristics of a diamond (especially the price, since that's our focus) change based on its color. Remember that you can use the `groupby()` method in pandas. 
# 
# **Using the `describe()` method, take a look on the dataset paying special attention to the variability. Comment what you see.**

# In[3]:


diamonds.describe()


# In[4]:


#your code here
#Group by 'price'
diamonds.groupby(['color'])['price'].mean()


# In[ ]:


#your comments here
Products with the color G are the closer to the mean with 3999.135671. -3932.799722	


# Let's proceed to check each feature separately. 
# 
# **Before starting, which features do you think that will affect the price most and why? You will contrast your hypotheses with your results.**

# In[ ]:


#your hypotheses here

The price is affected by the carat, the cut, the color, the clarity and the depth. 


# ## 1. The `color` column
# First, let's look at the color column.
# 
# **For each different color, find the mean of each column. You should have a matrix with every color as rows and the columns `carat`, `clarity`, etc as columns.**

# In[6]:


#your code here
CL = diamonds.groupby('color').mean()
CL


# **What do you see? Pay special attention to the relationship between price and color.**

# In[ ]:


#your thoughts here
The color has an impact on the price.


# Let's go further into the color feature. We will plot the frequency distribution of the diamonds color in our dataset. 
# 
# **Plot the distribution and analyze it. Remember that you can use the pandas `plot()` method.**

# In[23]:


#your code here
CL.plot(kind='pie', y='price', autopct='%1.0f%%', title='Price per color')


# In[ ]:


#your comments here
The colors I and J have almost the same prize and are the most expensive.


# ## 2.The `carat` column 

# Let's check the `carat` (weight), since this could also be a potential factor for price change.
# 
# **Find the mean of each column for each value of `carat` using the `groupby` method. Then comment your results.**

# In[25]:


#your code here
CRT = diamonds.groupby('carat').mean()
CRT


# In[ ]:


#your comments
The price depends of the carat.


# 
# **Plot a histogram of the `carat` column by using the `plot` method (see the docs to find an easy way to do so). What is happening?**

# In[31]:


#your code here
pd.CRT.plot(kind = 'hist')


# # 3. The `table` and `clarity` column
# Finally, let's check the `table`.
# 
# **Find the mean of each column for each value of `table` using the `groupby` method. Then comment your results.**

# In[32]:


#your code here
diamonds.groupby('table').mean()


# In[ ]:


#your comments here


# **Finally, do the same with the `clarity` column.**

# In[33]:


#your code here
diamonds.groupby('clarity').mean()


# In[ ]:


#your comments here


# **After looking at your results, which features do you think will affect price the most now? Regarding your hypotheses, do they match your final results? Provide a small overview.**

# In[ ]:


#your thoughts here


# # Bonus: taking a deeper look with plots and correlations
# 
# To take deeper look, we will use the `pairplot` method of `seaborn` library. This method plots a scatterplot for each pair of features and in the diagonal the distribution of the feature.
# 
# So if you have many features it will take a while, be careful!
# 

# In[35]:


#Run this code
import seaborn as sns
sns.pairplot(diamonds, diag_kind = 'kde', plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'})


# **What do you see here? What relationships between variables are the most interesting?**

# In[ ]:


#your thoughts here


# Now we will see a correlation matrix with a plot. As you know a higher correlation means that the feature could be an effect (**but is not for sure**) for the changes on the price.
# 
# We will see this with a matrix with colors. A lighter color means greater correlation. 
# 
# This is done with the `seaborn` library as well.

# In[36]:


#Run this code
plt.figure(figsize=(20, 20))
p = sns.heatmap(diamonds.corr(), annot=True, square=True)


# **What do you see here? Regarding the results before, does it fit with them?**

# In[ ]:


#your thoughts here


# Finally, we will calculate the linear regression between the price and the weight. This will be done first by plotting it with the `seaborn` library and then calculating the error with the `scipy` library.

# In[37]:


#Run this code
plt.figure(figsize=(10, 10))
sns.regplot(diamonds.carat, diamonds.price, scatter=True)


# In[38]:


#Run this code
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(diamonds.carat, diamonds.price)
r2 = r_value ** 2
r2


# **What do you think?**

# In[ ]:


#your thoughts here


# **Would you do any other checks on other features? Do you have any comments regarding `carat`?**

# In[ ]:


#your thoughts here


# **Conlcusion**

# **From our dataset** we can conclude that although `color` and `clarity` have a classification, and thus an assigned importance or weight, they do not influence the monetary value of a diamond in determining way. While it is true that different colors or clarities may have different prices, upon closer examination those variations in price seem to be linked to `carat` (weight) and its `dimensions`. In our analysis, the key factor to determining a diamond's value was placed solely in the aforementioned features, since we can see in our correlation coefficients and in the coefficient of determination that these features are closely related.
