#!/usr/bin/env python
# coding: utf-8

# # Loops
# 
# Complete the following set of exercises to solidify your knowledge for Loops.

# #### 1. Print first 10 natural numbers using while loop

# In[5]:


i=1
while i < 11:
    print(i)
    i =i+1


# #### 2. Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# 
# The number must be divisible by five
# 
# If the number is greater than 150, then skip it and move to the next number
# 
# If the number is greater than 500, then stop the loop
# 
# numbers = [12, 75, 150, 180, 145, 525, 50]

# In[16]:


numbers = [12, 75, 150, 180, 145, 525, 50]
len(numbers)
for elements in range (len(numbers)):
    if numbers[elements] % 5 == 0:
        if numbers[elements]  > 150:
            print("greater >150:" ,numbers[elements]  )
            continue
        elif numbers[elements]  > 500:
            break
        else:
            continue
 


# #### 3.Write a Python program to check the validity of a password (input from users).
# 
# Validation :
# 
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# 
# At least 1 number between [0-9].
# 
# At least 1 character from [$#@].
# 
# Minimum length 6 characters.
# 
# Maximum length 16 characters.

# In[ ]:


import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")


# #### 4. Break the loop when x is 6, and see what happens with the else block

# In[20]:


for i in range(10):
    print(i)
    if i == 6:
        break
    


# #### 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
# 

# In[22]:


x = int(input("Enter the first number:"))
sum=x
i=1
while x!=0:
    x=int(input ("input"))
    sum=sum+x
    i=i+1
print(sum)
print(sum/i)
 


# In[ ]:




