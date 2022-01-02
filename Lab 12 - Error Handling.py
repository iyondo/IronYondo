#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# In[2]:


# Libraries
import math


# # Challenge 1 - Handling Errors Using `if` Statements
# 
# In many cases, we are able to identify issues that may come up in our code and handle those handlful of issues with an `if` statment. Sometimes we would like to handle different types of inputs and are aware that later in the code, we will have to write two different branches of code for the two different cases we allowed in the beginning.
# 
# In the 3 cells below, add an `if` statment that will handle both types of input allowed in the functions.

# In[19]:


# Modify the code below to handle positive and negative numbers by adding an if statement and performing a transformation:



from cmath import sqrt
def sqrt_for_all(x):
    """
    This function will take any real number and 
    return the square root of its magnitude.
    
    Input: Real number
    Output: Real number
    
    Sample Input: -4
    Sample Output: 2.0
    """
    if x > 0:
        return math.sqrt(x)
    else:
        return math.sqrt(-x)

print(sqrt_for_all(-1))
print(sqrt_for_all(-4))
print(sqrt_for_all(4))


# In[14]:


# Modify the code below to handle zero as well. In the case of zero, return zero

def divide(x, y):
    """
    This function will take any two real numbers 
    and return their quotient. 
    If the denominator is zero, we return zero.
    
    Input: Real number
    Output: Real number
    
    Sample Input: 5, 1
    Sample Output: 5.0
    """
    if y != 0:
        return x / y
    else:
        return 0

print(divide(5, 0))
print(divide(5, 5))


# In[ ]:


# Modify the function below that it will take either an number and a list or two numbers. 
# If we take two numbers, add them together and return a list of length 1. 
# Otherwise, add the number to every element of the list and return the resulting list

def add_elements(a, l):
    """
    This function takes either two numbers or a list and a number 
    and adds the number to all elements of the list.
    If the function only takes two numbers, it returns a list 
    of length one that is the sum of the numbers.
    
    Input: number and list or two numbers
    Output: list
    
    Sample Input: 5, 6
    Sample Output: [11]
    """
    
    return [a + element for element in l]
        
add_elements(5, 6)


# # Challenge 2 - Fixing Errors to Get Code to Run
# 
# Sometimes the error is not caused by the input but by the code itself. In the 2 following cells below, examine the error and correct the code to avoid the error.

# In[21]:


# Modify the code below:

l = [1,2,3,4]

sum([element + 1 for element in l]) # parenthese missing


# In[47]:


# Modify the code below:

l = [1,2,3,4]

for element in l:
    print("The current element in the loop is", (element)) #we need to add the coma and element in parantheses


# # Bonus Challenge - Raise Errors on Your Own
# 
# There are cases where you need to alert your users of a problem even if the input will not immediately produce an error. In these cases you may want to throw an error yourself to bring attention to the problem. In the 2 cells below, write the functions as directed and add the appropriate errors using the `raise` clause. Make sure to add a meaningful error message.

# In[9]:


import math

def log_square(x):
    """
    This function takes a numeric value and returns the 
    natural log of the square of the number.
    The function raises an error if the number is equal to zero.
    Use the math.log function in this funtion.
    
    Input: Real number
    Output: Real number or error
    
    Sample Input: 5
    Sample Output: 3.21887
    """
 
    # Your code here:
    if x == 0:
        raise ValueError ("The number is equal to zero!")
    else: 
        print (math.log(x**2))

        
print(log_square(2))
print(log_square(1))
    


# In[73]:


import re

def check_capital(x):
    """
    This function returns true if the string contains 
    at least one capital letter and throws an error otherwise.
    
    Input: String
    Output: Bool or error message
    
    Sample Input: 'John'
    Sample Output: True
    """
    
    # Your code here
    for x in text:
        if len(re.findall([A-Z], text)) > 0:
            print(True)
        else:
            raise ValuerError ("There is not one capital letter")
     
 
check_capital(John)
        

