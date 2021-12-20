#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# # Challenge - Passing a Lambda Expression to a Function
# 
# In the next excercise you will create a function that returns a lambda expression. Create a function called `modify_list`. The function takes two arguments, a list and a lambda expression. The function iterates through the list and applies the lambda expression to every element in the list.

# In[42]:


def modify_list(lst, lmbda):
    """
    Input: list and lambda expression
    Output: the transformed list
    """
    
    # your code here
    lmbda = lambda x: x**2
    w = [lmbda(x) for x in lst
    print(w)
  


# In[40]:


lst = [1,5,8,10]

lmbda = lambda x: x**2
w = [lmbda(x) for x in lst]
print(w)


# #### Now we will define a lambda expression that will transform the elements of the list. 
# 
# In the cell below, create a lambda expression that converts Celsius to Kelvin. Recall that 0°C + 273.15 = 273.15K

# In[38]:


# your code here
a = lambda x: x + 273.15


# Finally, convert the list of temperatures below from Celsius to Kelvin.

# In[39]:


temps = [12, 23, 38, -55, 24]

# your code here

convert = lambda x: x+273.15
temperature = [convert(x) for x in temps]
print(temperature)


# #### In this part, we will define a function that returns a lambda expression
# 
# In the cell below, write a lambda expression that takes two numbers and returns 1 if one is divisible by the other and zero otherwise. Call the lambda expression `mod`.

# In[ ]:


# your code here

mod = lambda num, denom : "1" if (num % denom == 0) else "0"

print(mod(10,5))
print(mod(8,3))



# #### Now create a function that returns mod. The function only takes one argument - the first number in the `mod` lambda function. 
# 
# Note: the lambda function above took two arguments, the lambda function in the return statement only takes one argument but also uses the argument passed to the function.

# In[26]:


def divisor(b):
    """
    Input: a number
    Output: a function that returns 1 if the number is 
    divisible by another number (to be passed later) and zero otherwise.
    """
    
    # your code here
    num = int(input("Enter a number"))
    denom = int(input("Enter a number"))
    return lambda num, denom : "1" if (num % denom == 0) else "0"

         
    
    


# Finally, pass the number 5 to `divisor`. Now the function will check whether a number is divisble by 5. Assign this function to `divisible5`

# In[130]:


# your code here
divisible5 == divisor(5)


# Test your function with the following test cases:

# In[20]:


divisible5(10)


# In[ ]:


divisible5(8)


# # Bonus Challenge - Using Lambda Expressions in List Comprehensions
# 
# In the following challenge, we will combine two lists using a lambda expression in a list comprehension. 
# 
# To do this, we will need to introduce the `zip` function. The `zip` function returns an iterator of tuples.

# In[10]:


# Here is an example of passing one list to the zip function. 
# Since the zip function returns an iterator, we need to evaluate the iterator by using a list comprehension.

l = [1,2,3,4,5]
[x for x in zip(l)]


# Using the `zip` function, let's iterate through two lists and add the elements by position.

# In[47]:


list1 = ['Green', 'cheese', 'English', 'tomato']
list2 = ['eggs', 'cheese', 'cucumber', 'tomato']

# your code here
x = zip(list1, list2)

print(tuple(x)) #use the tuple() function to display a readable version of the result


# # Bonus Challenge - Using Lambda Expressions as Arguments
# 
# #### In this challenge, we will zip together two lists and sort by the resulting tuple.
# 
# In the cell below, take the two lists provided, zip them together and sort by the first letter of the second element of each tuple. Do this using a lambda function.

# In[63]:


list1 = ['Engineering', 'Computer Science', 'Political Science', 'Mathematics']
list2 = ['Lab', 'Homework', 'Essay', 'Module']

# your code here
x = zip(list1, list2)
w = list(x)

print(w)

w.sort(key=lambda y: y[0])

print(w)


# # Bonus Challenge - Sort a Dictionary by Values
# 
# Given the dictionary below, sort it by values rather than by keys. Use a lambda function to specify the values as a sorting key.

# In[18]:


d = {'Honda': 1997, 'Toyota': 1995, 'Audi': 2001, 'BMW': 2005}
d_list = sorted(d.items(), key=lambda x:x[1])
sortdict = dict(d_list)
print(sortdict)



# your code here

