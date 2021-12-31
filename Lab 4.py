#!/usr/bin/env python
# coding: utf-8

# # List Comprehensions
# 
# Complete the following set of exercises to solidify your knowledge of list comprehensions.

# In[1]:


import os;


# #### 1. Use a list comprehension to create and print a list of consecutive integers starting with 1 and ending with 50.

# In[2]:


#1st method:
lst = []
for i in range(51):
    lst.append(i)

print(lst)


# In[3]:


#2nd method:
lst = [i for i in range(51)]
print(lst)


# #### 2. Use a list comprehension to create and print a list of even numbers starting with 2 and ending with 200.

# In[4]:


lst = [i for i in range(201) if i>0 and i%2 == 0]
print(lst)


# #### 3. Use a list comprehension to create and print a list containing all elements of the 10 x 4 array below.

# In[5]:


a = [[0.84062117, 0.48006452, 0.7876326 , 0.77109654],
       [0.44409793, 0.09014516, 0.81835917, 0.87645456],
       [0.7066597 , 0.09610873, 0.41247947, 0.57433389],
       [0.29960807, 0.42315023, 0.34452557, 0.4751035 ],
       [0.17003563, 0.46843998, 0.92796258, 0.69814654],
       [0.41290051, 0.19561071, 0.16284783, 0.97016248],
       [0.71725408, 0.87702738, 0.31244595, 0.76615487],
       [0.20754036, 0.57871812, 0.07214068, 0.40356048],
       [0.12149553, 0.53222417, 0.9976855 , 0.12536346],
       [0.80930099, 0.50962849, 0.94555126, 0.33364763]];


# In[6]:


lsta = [i for i in a]
print(lsta)


# #### 4. Add a condition to the list comprehension above so that only values greater than or equal to 0.5 are printed.

# In[7]:


#1st method: from the matrice a
lst_a = [x for i in a for x in i if x >= 0.5]
lst_a


# In[8]:


#2nd method: from the list: lsta
lst_c = [x for i in lsta for x in i if x >= 0.5]
lst_c


# #### 5. Use a list comprehension to create and print a list containing all elements of the 5 x 2 x 3 array below.

# In[9]:


b = [[[0.55867166, 0.06210792, 0.08147297],
        [0.82579068, 0.91512478, 0.06833034]],

       [[0.05440634, 0.65857693, 0.30296619],
        [0.06769833, 0.96031863, 0.51293743]],

       [[0.09143215, 0.71893382, 0.45850679],
        [0.58256464, 0.59005654, 0.56266457]],

       [[0.71600294, 0.87392666, 0.11434044],
        [0.8694668 , 0.65669313, 0.10708681]],

       [[0.07529684, 0.46470767, 0.47984544],
        [0.65368638, 0.14901286, 0.23760688]]];


# In[10]:


lstb =[i for i in b]
print(lstb)


# #### 6. Add a condition to the list comprehension above so that the last value in each subarray is printed, but only if it is less than or equal to 0.5.

# In[19]:


lst_b = [x[-1] for i in b for x in i if x[-1] <= 0.5]

lst_b


# #### 7. Use a list comprehension to select and print the names of all CSV files in the */data* directory.

# In[ ]:


file_list = [f for f in os.listdir('Documents') if f.endswith('.csv')]
file_list


# ### Bonus

# Try to solve these katas using list comprehensions.

# **Easy**
# - [Insert values](https://www.codewars.com/kata/invert-values)
# - [Sum Square(n)](https://www.codewars.com/kata/square-n-sum)
# - [Digitize](https://www.codewars.com/kata/digitize)
# - [List filtering](https://www.codewars.com/kata/list-filtering)
# - [Arithmetic list](https://www.codewars.com/kata/541da001259d9ca85d000688)
# 
# **Medium**
# - [Multiples of 3 or 5](https://www.codewars.com/kata/514b92a657cdc65150000006)
# - [Count of positives / sum of negatives](https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives)
# - [Categorize new member](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa)
# 
# **Advanced**
# - [Queue time counter](https://www.codewars.com/kata/queue-time-counter)
