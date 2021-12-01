#!/usr/bin/env python
# coding: utf-8

# ## Challenge 2: Sets
# 
# There are a lot to learn about Python Sets and the information presented in the lesson is limited due to its length. To learn Python Sets in depth you are strongly encouraged to review the W3Schools tutorial on [Python Sets Examples and Methods](https://www.w3schools.com/python/python_sets.asp) before you work on this lab. Some difficult questions in this lab have their solutions in the W3Schools tutorial.
# 
# #### First, import the Python `random` library.

# In[ ]:


import random


# #### In the cell below, create a list named `sample_list_1` with 80 random values. 
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * Each value in the list is unique.
# 
# Print `sample_list_1` to review its values
# 
# *Hint: use `random.sample` ([reference](https://docs.python.org/3/library/random.html#random.sample)).*

# In[17]:


import random
L = list(range(100))
sample_list_1 = random.sample(L,80)

print(sample_list_1)


# In[ ]:


import random


# #### Convert `sample_list_1` to a set called `set1`. Print the length of the set. Is its length still 80?

# In[13]:


import random
L = list(range(100))
sample_list_1 = random.sample(L,80)
set1 = set(sample_list_1)
len(set1)


# #### Create another list named `sample_list_2` with 80 random values.
# 
# Requirements:
# 
# * Each value is an integer falling between 0 and 100.
# * The values in the list don't have to be unique.
# 
# *Hint: Use a FOR loop.*

# In[9]:


import random
sample_list_2 = [random.randint(0,100) for i in range(80)]
print(sample_list_2)


# #### Convert `sample_list_2` to a set called `set2`. Print the length of the set. Is its length still 80?

# In[21]:


import random
L = list(range(100))
sample_list_2 = random.sample(L,80)
print(sample_list_2)
set2 = set(sample_list_2)
sample_list_2 = set2
print(set2)
len(set2)


# #### Identify the elements present in `set1` but not in `set2`. Assign the elements to a new set named `set3`.

# In[48]:



set3 = set1-set2
print(set3)


# #### Identify the elements present in `set2` but not in `set1`. Assign the elements to a new set named `set4`.

# In[45]:


# Your code here
set4 = (set(sample_list_2) - set(sample_list_1))
print(set4)


# #### Now Identify the elements shared between `set1` and `set2`. Assign the elements to a new set named `set5`.

# In[51]:


set5 = set2.intersection(set1)
print(set5)


# #### What is the relationship among the following values:
# 
# * len(set1)
# * len(set2)
# * len(set3)
# * len(set4)
# * len(set5)
# 
# Use a math formular to represent that relationship. Test your formular with Python code.

# In[ ]:


len(x)


# #### Create an empty set called `set6`.

# In[55]:


# Your code here
set6 = set()
print(set6)


# #### Add `set3` and `set5` to `set6` using the Python Set `update` method.

# In[112]:


set3
print(set3)
set5
print(set5)
set6
print(set6)

result1 = set3.update(set6)
print(result1)

result2 = set5.update(result1)
print(result2)


# #### Check if `set1` and `set6` are equal.

# In[94]:


for i in set1:
    if i not in set6:
        print("set1 and set6 are not equal")
    else:
        print("set1 and set6 are not equal")


# #### Check if `set1` contains `set2` using the Python Set `issubset` method. Then check if `set1` contains `set3`.*

# In[82]:


result1 = set1.issubset(set2)
print(result1)
result2 = set1.issubset(set3)
print(result2)


# #### Using the Python Set `union` method, aggregate `set3`, `set4`, and `set5`. Then aggregate `set1` and `set2`. 
# 
# #### Check if the aggregated values are equal.

# In[90]:


Union1 = set3.union(set4, set5) 
print(Union1)


# In[92]:


Union2 = set1.union(set2)
print(Union2)


# #### Using the `pop` method, remove the first element from `set1`.

# In[70]:


set1
print(set1)
set1.pop()
print(set1)


# #### Remove every element in the following list from `set1` if they are present in the set. Print the remaining elements.
# 
# ```
# list_to_remove = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
# ```

# In[106]:


# Your code here
set1
print(set1)
R = [1, 9, 11, 19, 21, 29, 31, 39, 41, 49, 51, 59, 61, 69, 71, 79, 81, 89, 91, 99]
print(R)
Remain= set1.difference(R)
print(Remain)



