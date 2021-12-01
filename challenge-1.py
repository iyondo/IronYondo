#!/usr/bin/env python
# coding: utf-8

# ## Challenge 1: Tuples
# 
# #### Do you know you can create tuples with only one element?
# 
# **In the cell below, define a variable `tup` with a single element `"I"`.**
# 
# *Hint: you need to add a comma (`,`) after the single element.*

# In[5]:


tup =("I",)


# #### Print the type of `tup`. 
# 
# Make sure its type is correct (i.e. *tuple* instead of *str*).

# In[6]:


type(tup)


# #### Now try to append the following elements to `tup`. 
# 
# Are you able to do it? Explain.
# 
# ```
# "r", "o", "n", "h", "a", "c", "k',
# ```

# In[1]:


tup = ("r", "o", "n", "h", "a", "c", "k',)
       append(tup)
print(tup)

# Your explanation here


# #### How about re-assign a new value to an existing tuple?
# 
# Re-assign the following elements to `tup`. Are you able to do it? Explain.
# 
# ```
# "I", "r", "o", "n", "h", "a", "c", "k"
# ```

# In[ ]:


tup = ("I", "r", "o", "n", "h", "a", "c", "k")


# #### Split `tup` into `tup1` and `tup2` with 4 elements in each. 
# 
# `tup1` should be `("I", "r", "o", "n")` and `tup2` should be `("h", "a", "c", "k")`.
# 
# *Hint: use positive index numbers for `tup1` assignment and use negative index numbers for `tup2` assignment. Positive index numbers count from the beginning whereas negative index numbers count from the end of the sequence.*
# 
# Also print `tup1` and `tup2`.

# In[ ]:


tup = ("I", "r", "o", "n", "h", "a", "c", "k")
 


# #### Add `tup1` and `tup2` into `tup3` using the `+` operator.
# 
# Then print `tup3` and check if `tup3` equals to `tup`.

# In[16]:


tup1 = ("I", "r", "o", "n")
tup2 = ("h", "a", "c", "k")
tup3 = tup1 + tup2
print(tup3)
len(tup3)


# #### Count the number of elements in `tup1` and `tup2`. Then add the two counts together and check if the sum is the same as the number of elements in `tup3`.

# In[15]:


tup1 = ("I", "r", "o", "n")
print(tup1)
len(tup1)


# In[13]:


tup2 = ("h", "a", "c", "k")
print(tup2)
len(tup2)


# In[20]:


result = tup1 + tup2
print(result)
len(result)


# #### What is the index number of `"h"` in `tup3`?

# In[27]:


tup3
print(tup3)
i = tup3.index("h")
print(i)


# #### Now, use a FOR loop to check whether each letter in the following list is present in `tup3`:
# 
# ```
# letters = ["a", "b", "c", "d", "e"]
# ```
# 
# For each letter you check, print `True` if it is present in `tup3` otherwise print `False`.
# 
# *Hint: you only need to loop `letters`. You don't need to loop `tup3` because there is a Python operator `in` you can use. See [reference](https://stackoverflow.com/questions/17920147/how-to-check-if-a-tuple-contains-an-element-in-python).*

# In[38]:


for i in letters:
    if i in tup3:
        print("True")
    else:
        print("false")


# #### How many times does each letter in `letters` appear in `tup3`?
# 
# Print out the number of occurrence of each letter.

# In[ ]:


for i in letters:
    count()

