#!/usr/bin/env python
# coding: utf-8

# # Understanding Descriptive Statistics
# 
# Import the necessary libraries here:
. If they are close in value, it means that the data is symmetrically distributed around the mean. If the mean is greater than the median, our data is right skewed. If the median is greater than the mean, the data is left skewed.
# In[1]:


# Libraries
import numpy as np
import pandas as pd
import random
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Challenge 1
# #### 1.- Define a function that simulates rolling a dice 10 times. Save the information in a dataframe.
# **Hint**: you can use the *choices* function from module *random* to help you with the simulation.

# In[2]:


# your code here
l=[]
def roll(x):
    for i in range(x):
        y=random.choice(range(1, 7))
        l.append(y)
        
    return l

    
roll(10)


# In[3]:


l


# In[4]:


#Information into Dataframe
dd=pd.DataFrame(roll(10))
dd.head()


# In[5]:


dd.columns


# In[6]:


#Add the column name 'value' so we can sort it out later
dd.columns =['value']
dd.head()


# #### 2.- Plot the results sorted by value.

# In[7]:


# your code here
sort_lst = dd.sort_values(by ='value')
sort_lst


# In[8]:


sort_lst.plot()


# #### 3.- Calculate the frequency distribution and plot it. What is the relation between this plot and the plot above? Describe it with words.

# In[9]:


# your code here
frequency = sort_lst['value'].value_counts()
frequency


# In[10]:


frequency.plot()


# In[ ]:


"""
your comments here
"""
The second plot is regarding the cumulative values.


# ## Challenge 2
# Now, using the dice results obtained in *challenge 1*, your are going to define some functions that will help you calculate the mean of your data in two different ways, the median and the four quartiles. 
# 
# #### 1.- Define a function that computes the mean by summing all the observations and dividing by the total number of observations. You are not allowed to use any methods or functions that directly calculate the mean value. 

# In[12]:


# your code here
from functools import reduce
 
def mymean(sort_lst):
    x = (reduce(lambda a, b: a + b, l)) / len(sort_lst)
    return x
    


# In[ ]:


#Example mean - l = [10, 12, 34, 23]
# from functools import reduce
# x = (reduce(lambda a, b: a + b, l)) / len(l)


# #### 2.- First, calculate the frequency distribution. Then, calculate the mean using the values of the frequency distribution you've just computed. You are not allowed to use any methods or functions that directly calculate the mean value. 

# In[13]:


# your code here
frequency.describe()


# In[15]:


mymean(sort_lst)


# #### 3.- Define a function to calculate the median. You are not allowed to use any methods or functions that directly calculate the median value. 
# **Hint**: you might need to define two computation cases depending on the number of observations used to calculate the median.

# In[ ]:


# your code here


# #### 4.- Define a function to calculate the four quartiles. You can use the function you defined above to compute the median but you are not allowed to use any methods or functions that directly calculate the quartiles. 

# In[ ]:


# your code here


# ## Challenge 3
# Read the csv `roll_the_dice_hundred.csv` from the `data` folder.
# #### 1.- Sort the values and plot them. What do you see?

# In[16]:


# your code here
hundred = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Labs 4\roll_the_dice_hundred.csv')
hundred.head()


# In[17]:


#DF sort by values
top_lst = hundred.sort_values(by=['value'])
top_lst


# In[18]:


top_lst['value'].plot()


# In[19]:


top_lst.describe()


# In[ ]:


"""
your comments here
"""


# #### 2.- Using the functions you defined in *challenge 2*, calculate the mean value of the hundred dice rolls.

# In[ ]:


# your code here


# #### 3.- Now, calculate the frequency distribution.
# 

# In[20]:


# your code here
frequency = hundred['value'].value_counts()
frequency


# #### 4.- Plot the histogram. What do you see (shape, values...) ? How can you connect the mean value to the histogram? 

# In[21]:


# your code here
top_lst['value'].hist()


# In[ ]:


"""
your comments here
"""


# #### 5.- Read the `roll_the_dice_thousand.csv` from the `data` folder. Plot the frequency distribution as you did before. Has anything changed? Why do you think it changed?

# In[22]:


# your code here
thousand = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Labs 4\roll_the_dice_thousand.csv')
thousand.head()


# In[23]:


#DF sort by values
top_lst1 = thousand.sort_values(by=['value'])
top_lst1


# In[24]:


frequency = thousand['value'].value_counts()
frequency


# In[25]:


top_lst1['value'].plot()


# In[26]:


thousand.describe()


# In[ ]:


"""
your comments here
"""


# ## Challenge 4
# In the `data` folder of this repository you will find three different files with the prefix `ages_population`. These files contain information about a poll answered by a thousand people regarding their age. Each file corresponds to the poll answers in different neighbourhoods of Barcelona.
# 
# #### 1.- Read the file `ages_population.csv`. Calculate the frequency distribution and plot it as we did during the lesson. Try to guess the range in which the mean and the standard deviation will be by looking at the plot. 

# In[27]:


# your code here
age = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Labs 4\ages_population.csv')
age.head()


# In[28]:


frequency = age['observation'].value_counts()
frequency


# In[29]:


age.plot()


# In[30]:


age.describe()


# #### 2.- Calculate the exact mean and standard deviation and compare them with your guesses. Do they fall inside the ranges you guessed?

# In[31]:


# your code here
mean =  age.mean()
std = age.std()
median = age.median()

print('the mean is ', mean) 
print('the std is ', std)
print('the median is ', median)


# In[32]:


age.describe()


# In[ ]:


"""
your comments here

"""

print('the difference between the median is: ', median - mean)
The median and the mean are close in value, it means that the data is symmetrically distributed around the mean.


# #### 3.- Now read the file `ages_population2.csv` . Calculate the frequency distribution and plot it.

# In[33]:


# your code here
age2 = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Labs 4\ages_population2.csv')
age2.head()


# In[34]:


age2.describe()


# In[35]:


frequency = age2['observation'].value_counts()
frequency


# ####  4.- What do you see? Is there any difference with the frequency distribution in step 1?

# In[ ]:


"""
your comments here
"""
The median and the mean are close in value, it means that the data is symmetrically distributed around the mean.


# #### 5.- Calculate the mean and standard deviation. Compare the results with the mean and standard deviation in step 2. What do you think?

# In[ ]:


# your code here


# In[ ]:


"""
your comments here
"""


# ## Challenge 5
# Now is the turn of `ages_population3.csv`.
# 
# #### 1.- Read the file `ages_population3.csv`. Calculate the frequency distribution and plot it.

# In[37]:


# your code here
age3 = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Labs 4\ages_population3.csv')
age3.head()


# In[38]:


frequency = age3['observation'].value_counts()
frequency


# In[39]:


age3.plot()


# #### 2.- Calculate the mean and standard deviation. Compare the results with the plot in step 1. What is happening?

# In[40]:


# your code here
mean = age3.mean()
std = age3.std()

print('mean', mean)
print('std', std)

"""
your comments here
"""
The mean is 42 and the standard deviation is 16,1.
# #### 3.- Calculate the four quartiles. Use the results to explain your reasoning for question in step 2. How much of a difference is there between the median and the mean?

# In[42]:


# your code here

q1 = age3.quantile(0.25)
median = age3.quantile(0.50)
q3 = age3.quantile(0.75)

print('25th', q1)
print('50th or median', median)
print('75th', q3)


# In[43]:


age3.quantile([0.25, 0.5,0.75])


# In[ ]:


"""
your comments here
"""


print('the difference betwwen the mean and the median is: ', mean - median)
The median and the mean are close in value, it means that the data is symmetrically distributed around the mean.


# #### 4.- Calculate other percentiles that might be useful to give more arguments to your reasoning.

# In[44]:


# your code here
age3.describe()


# In[ ]:


"""
your comments here
"""


# ## Bonus challenge
# Compare the information about the three neighbourhoods. Prepare a report about the three of them. Remember to find out which are their similarities and their differences backing your arguments in basic statistics.

# In[ ]:


# your code here


# In[ ]:


"""
your comments here
"""

