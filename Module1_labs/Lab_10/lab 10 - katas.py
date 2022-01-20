#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Count sheeps
T = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
True_l = T.count(True)
print(True_l)


# In[ ]:


#Removing elements
Text = ["Keep", "Remove", "Keep", "Remove", "Keep"]
def remove_every_other(my_list):
    return Text.pop(2)


# In[ ]:


#Convert number to reversed array of digits
number = input("Input a number: ")
for char in range(len(number) - 1, -1, -1):
  print(number[char], end="")
print("\n")


# In[14]:


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
def square_digits(num):
    return (x**2+y**2)

square_digits(52)

