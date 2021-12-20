#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# In[8]:


# Import reduce from functools, numpy and pandas
from functools import reduce
import numpy as np
import pandas as pd


# # Challenge 1 - Mapping
# 
# #### We will use the map function to clean up words in a book.
# 
# In the following cell, we will read a text file containing the book The Prophet by Khalil Gibran.

# In[1]:


# Run this code:

location = r'C:\Users\Ingrid\IronHack\DAFT_NOV_21_01\module_1\Lab_26 Map-Reduce-Filter/58585-0.txt' #on met r devant pour inverser le sens des slashs
with open(location, 'r', encoding="utf8") as f:
    prophet = f.read().split(' ')


# #### Let's remove the first 568 words since they contain information about the book but are not part of the book itself. 
# 
# Do this by removing from `prophet` elements 0 through 567 of the list (you can also do this by keeping elements 568 through the last element).

# In[2]:


# your code here
# keeping elements 568 through the last element
cut_list1 = prophet[568:]
print(cut_list1)


# In[5]:


n_prophet = list(filter(lambda x: prophet.index(x) > 567, prophet))
n_prophet


# If you look through the words, you will find that many words have a reference attached to them. For example, let's look at words 1 through 10.

# In[17]:


# your code here
new_list = []
for index in range(0,10):
    new_list.append(prophet[index])
print(new_list)


# #### The next step is to create a function that will remove references. 
# 
# We will do this by splitting the string on the `{` character and keeping only the part before this character. Write your function below.

# In[ ]:


def reference(x):
    '''
    Input: A string
    Output: The string with references removed
    
    Example:
    Input: 'the{7}'
    Output: 'the'
    '''
    
    # your code here
    prophet.remove{)
    print(prophet)


# Now that we have our function, use the `map()` function to apply this function to our book, The Prophet. Return the resulting list to a new list called `prophet_reference`.

# In[ ]:


# your code here


# Another thing you may have noticed is that some words contain a line break. Let's write a function to split those words. Our function will return the string split on the character `\n`. Write your function in the cell below.

# In[ ]:


def line_break(x):
    '''
    Input: A string
    Output: A list of strings split on the line break (\n) character
        
    Example:
    Input: 'the\nbeloved'
    Output: ['the', 'beloved']
    '''
    
    # your code here


# Apply the `line_break` function to the `prophet_reference` list. Name the new list `prophet_line`.

# In[ ]:


# your code here


# If you look at the elements of `prophet_line`, you will see that the function returned lists and not strings. Our list is now a list of lists. Flatten the list using list comprehension. Assign this new list to `prophet_flat`.

# In[ ]:


# your code here


# # Challenge 2 - Filtering
# 
# When printing out a few words from the book, we see that there are words that we may not want to keep if we choose to analyze the corpus of text. Below is a list of words that we would like to get rid of. Create a function that will return false if it contains a word from the list of words specified and true otherwise.

# In[22]:


def word_filter(x):
    '''
    Input: A string
    Output: True if the word is not in the specified list 
    and False if the word is in the list.
        
    Example:
    word list = ['and', 'the']
    Input: 'and'
    Output: False
    
    Input: 'John'
    Output: True
    '''
    
    word_list = ['and', 'the', 'a', 'an']
    
    # your code here
    
    for x in word_list:
        print(word_filter.append(x))
    else:
        print(False)

  


# Use the `filter()` function to filter out the words speficied in the `word_filter()` function. Store the filtered list in the variable `prophet_filter`.

# # Bonus Challenge
# 
# Rewrite the `word_filter` function above to not be case sensitive.

# In[ ]:


def word_filter_case(x):
   
    word_list = ['and', 'the', 'a', 'an']
    
    # your code here


# # Challenge 3 - Reducing
# 
# #### Now that we have significantly cleaned up our text corpus, let's use the `reduce()` function to put the words back together into one long string separated by spaces. 
# 
# We will start by writing a function that takes two strings and concatenates them together with a space between the two strings.

# In[ ]:


def concat_space(a, b):
    '''
    Input:Two strings
    Output: A single string separated by a space
        
    Example:
    Input: 'John', 'Smith'
    Output: 'John Smith'
    '''
    
    # your code here
    return a+" " +b


# Use the function above to reduce the text corpus in the list `prophet_filter` into a single string. Assign this new string to the variable `prophet_string`.

# In[ ]:


# your code here
prophet_string = 


# # Challenge 4 - Applying Functions to DataFrames
# 
# #### Our next step is to use the apply function to a dataframe and transform all cells.
# 
# To do this, we will connect to Ironhack's database and retrieve the data from the *pollution* database. Select the *beijing_pollution* table and retrieve its data.

# In[ ]:


# your code here


# Let's look at the data using the `head()` function.

# In[ ]:


# your code here


# The next step is to create a function that divides a cell by 24 to produce an hourly figure. Write the function below.

# In[ ]:


def hourly(x):
    '''
    Input: A numerical value
    Output: The value divided by 24
        
    Example:
    Input: 48
    Output: 2.0
    '''
    
    # your code here
   


# Apply this function to the columns `Iws`, `Is`, and `Ir`. Store this new dataframe in the variable `pm25_hourly`.

# In[ ]:


# your code here


# #### Our last challenge will be to create an aggregate function and apply it to a select group of columns in our dataframe.
# 
# Write a function that returns the standard deviation of a column divided by the length of a column minus 1. Since we are using pandas, do not use the `len()` function. One alternative is to use `count()`. Also, use the numpy version of standard deviation.

# In[ ]:


def sample_sd(x):
    '''
    Input: A Pandas series of values
    Output: the standard deviation divided by the number of elements in the series
        
    Example:
    Input: pd.Series([1,2,3,4])
    Output: 0.3726779962
    '''
    
    # your code here

