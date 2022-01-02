#!/usr/bin/env python
# coding: utf-8

# # Katas 1

# In[1]:


#Remove All The Marked Elements of a List
#Define a method/function that removes from a given array of integers all the values contained in a second array

def remove(list_1, list_2):
    return set(list_1) - set(list_2)

          
    


# In[2]:


list_1  =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
list_2 = [1, 3]
remove(list_1, list_2)


# In[3]:


list_1 = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
list_2 = [1, 3, 4, 2]
remove(list_1, list_2)
          


# In[4]:


list_1 = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
list_2 = [2, 4, 3]
remove(list_1, list_2)


# # Katas 2

# In[26]:


#Method For Counting Total Occurence Of Specific Digits


from collections import Counter

def count_spec_digits(integers_list, digits_list):
    for i in integers_list:
        for j in digits_lists:
            digits_list = integers_list.count
        


# In[27]:


integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]
count_spec_digits(integers_list, digits_list)


# In[29]:


integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list)


# In[ ]:


integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
l.count_spec_digits(integers_list, digits_list) 


# # Katas 3

# In[23]:


# Ordered Count of Characters
# Count the number of occurrences of each character and return it as a list of tuples in order of appearance. 
#For empty output return an empty list.

from collections import Counter


def ordered_count(text):
    frequency = Counter(text)
    for (key, value) in frequency.items():
        print( key, value)


# In[24]:


ordered_count("abracadabra")


# In[9]:


#Example
from collections import Counter

text = 'Mary had a little lamb'

frequency = Counter(text)

for (key, value) in frequency.items():
    print("Number of occurences of", key, "is", value)

