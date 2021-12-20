#!/usr/bin/env python
# coding: utf-8

# # Intrduction to NumPy
# 
# 
# #### 1. Import NumPy under the name np.

# In[3]:


# your code here
import numpy as np


# #### 2. Print your NumPy version.

# In[4]:


# your code here
print(np.__version__)


# #### 3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable *a*.
# **Challenge**: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

# In[8]:


#numpy array with random values
a= np.random.rand(2,3,5)



# In[6]:


# Method 2
#numpy array with random values
a1=np.random.random((2,3,5))
a1


# In[19]:


# Method 3


# #### 4. Print *a*.
# 

# In[18]:


print(a)


# #### 5. Create a 5x2x3 3-dimensional array with all values equaling 1. Assign the array to variable *b*.

# In[20]:


# your code here4 
b= np.ones((5, 2,3))


# #### 6. Print *b*.
# 

# In[21]:


# your code here
print(b)


# #### 7. Do *a* and *b* have the same size? How do you prove that in Python code?

# In[23]:


# your code here

import numpy as np 
 
a_size = np.size(a)
b_size = np.size(b)

 
print(a_size) 
print(b_size) 
print(a.size == b.size)


# #### 8. Are you able to add *a* and *b*? Why or why not?
# 

# In[ ]:


# your answer here
Yes


# #### 9. Transpose *b* so that it has the same structure of *a* (i.e. become a 2x3x5 array). Assign the transposed array to variable *c*.

# In[24]:


c = b.reshape(2,3,5)
print(c)


# #### 10. Try to add *a* and *c*. Now it should work. Assign the sum to variable *d*. But why does it work now?

# In[25]:


# your code/answer here
d = np.add(a, c)
print(d)


# #### 11. Print *a* and *d*. Notice the difference and relation of the two array in terms of the values? Explain.

# In[26]:


# your code/answer here

print(a)

print(d)

#Each value has +1 from c


# #### 12. Multiply *a* and *c*. Assign the result to *e*.

# In[27]:


# your code here
e = np.multiply(a,c)
e


# #### 13. Does *e* equal to *a*? Why or why not?
# 

# In[28]:


# your code/answer here
e==a


# #### 14. Identify the max, min, and mean values in *d*. Assign those values to variables *d_max*, *d_min* and *d_mean*.

# In[29]:


# your code here
d_max = print(np.max(d))
d_min = print(np.min(d))
d_mean = print(np.mean(d))


# #### 15. Now we want to label the values in *d*. First create an empty array *f* with the same shape (i.e. 2x3x5) as *d* using `np.empty`.
# 

# In[30]:


# your code here
f = np.empty([2,3,5])
print(f)


# #### 16. Populate the values in *f*. 
# 
# For each value in *d*, if it's larger than *d_min* but smaller than *d_mean*, assign 25 to the corresponding value in *f*. If a value in *d* is larger than *d_mean* but smaller than *d_max*, assign 75 to the corresponding value in *f*. If a value equals to *d_mean*, assign 50 to the corresponding value in *f*. Assign 0 to the corresponding value(s) in *f* for *d_min* in *d*. Assign 100 to the corresponding value(s) in *f* for *d_max* in *d*. In the end, f should have only the following values: 0, 25, 50, 75, and 100.
# 
# **Note**: you don't have to use Numpy in this question.

# In[35]:


# your code here
for l1 in range(0,2):
    for l2 in range(0,3):
        for el in range(0,5):
            if d_min<d[l1,l2,el]<d_mean:
                f[l1,l2,el]=25
            elif d_mean<d[l1,l2,el]<d_max:
                f[l1,l2,el]=75
            elif d[l1,l2,el]==d_mean:
                f[l1,l2,el]=50
            elif d[l1,l2,el]==d_min:
                f[l1,l2,el]=0
            elif d[l1,l2,el]==d_max:
                f[l1,l2,el]=100
print(f)


# In[37]:


# your code here


f = []
for x in np.nditer(d):
    if d_min < x < d_mean:
        f += [25]
    if d_mean < x < d_max:
        f += [75]
    if x == d_mean:
        f += [50]
    if x == d_min:
        f += [0]
    if x == d_max:
        f += [100]
    
        
f = np.reshape(f, d.shape) 
print(f)


# #### 17. Print *d* and *f*. Do you have your expected *f*?
# For instance, if your *d* is:
# ```python
# [[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
# [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
# [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
# [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
# [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
# [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]]
# ```
# Your *f* should be:
# ```python
# [[[ 75.,  75.,  75.,  25.,  75.],
# [ 75.,  75.,  25.,  25.,  25.],
# [ 75.,  25.,  75.,  75.,  75.]],
# [[ 25.,  25.,  25.,  25., 100.],
# [ 75.,  75.,  75.,  75.,  75.],
# [ 25.,  75.,   0.,  75.,  75.]]]
# ```

# In[ ]:


# your code here


# #### 18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), use string values  ("A", "B", "C", "D", and "E") to label the array elements. For the example above, the expected result is:
# 
# ```python
# [[[ 'D',  'D',  'D',  'B',  'D'],
# [ 'D',  'D',  'B',  'B',  'B'],
# [ 'D',  'B',  'D',  'D',  'D']],
# [[ 'B',  'B',  'B',  'B',  'E'],
# [ 'D',  'D',  'D',  'D',  'D'],
# [ 'B',  'D',   'A',  'D', 'D']]]
# ```
# **Note**: you don't have to use Numpy in this question.

# In[20]:


# your code here
f = []
for x in np.nditer(d):
    if d_min < x < d_mean:
        f += [A]
    if d_mean < x < d_max:
        f += [B]
    if x == d_mean:
        f += [C]
    if x == d_min:
        f += [D]
    if x == d_max:
        f += [F]
    
        
f = np.reshape(f, d.shape) 
print(f)


# In[ ]:




