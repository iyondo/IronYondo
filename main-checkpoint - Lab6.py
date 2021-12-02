#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# # Challenge 1 - Combining Strings
# 
# Combining strings is an important skill to acquire. There are multiple ways of combining strings in Python, as well as combining strings with variables. We will explore this in the first challenge. In the cell below, combine the strings in the list and add spaces between the strings (do not add a space after the last string). Insert a period after the last string.

# In[14]:


str_list = ['Durante', 'un', 'tiempo', 'no', 'estuvo', 'segura', 'de', 'si', 'su', 'marido', 'era', 'su', 'marido']
' '.join(str_list)+"."


# In the cell below, use the list of strings to create a grocery list. Start the list with the string `Grocery list: ` and include a comma and a space between each item except for the last one. Include a period at the end. Only include foods in the list that start with the letter 'b' and ensure all foods are lower case.

# In[21]:


food_list = ['Bananas', 'Chocolate', 'bread', 'diapers', 'Ice Cream', 'Brownie Mix', 'broccoli']
# Your code here:
Grocery = ' , '.join(food_list)+"."
print(Grocery.lower())
import re
m = re.findall(r'\bb\w+', Grocery)
print (m)
Grocery_list = " , ".join(m)+"."
print(Grocery_list)


# In[43]:


food_list = ['Bananas', 'Chocolate', 'bread', 'diapers', 'Ice Cream', 'Brownie Mix', 'broccoli']
# Your code here:
Grocery=[]
for food in food_list:
    if food.startswith('b') or food.startswith("B"):
        print(food)
        Grocery.append(food)
grocerylist=(" , ".join(Grocery))+"."
grocerylist=grocerylist.lower()
print(grocerylist)


# In the cell below, write a function that computes the area of a circle using its radius. Compute the area of the circle and insert the radius and the area between the two strings. Make sure to include spaces between the variable and the strings. 
# 
# Note: You can use the techniques we have learned so far or use f-strings. F-strings allow us to embed code inside strings. You can read more about f-strings [here](https://www.python.org/dev/peps/pep-0498/).

# In[ ]:


import math

string1 = "The area of the circle with radius:"
string2  = "is:"
radius = 4.5

def area(x, pi = math.pi):
    return 
    """
    This function takes a radius and returns the area of a circle. 
    We also pass a default value for pi.
    
    Input: Float (and default value for pi)
    Output: Float
    
    Sample input: 5.0
    Sample Output: 78.53981633
    """
    
    # Your code here:
def area(x, pi = math.pi): 
    return (" The area of the circle with radius: ", x,"is", pi * radius**2 )

pi * radius**2
    
# Your output string here:


# In[21]:


# Solution
import math
def area(x, pi = math.pi): 
    string1 = "The area of the circle with radius:"
    string2  = "is:"

    return (string1, x, string2, pi * x**2 )


# In[17]:


area(45,pi = math.pi)


# In[35]:


# Solution
import math
def area(x, pi = math.pi): 
    string1 = "The area of the circle with radius:"
    string2  = "is:"
    strip1 = string1.replace("'", " ")
    strip2 = string2.replace("'", " ")
    return (strip1, x, strip2, pi * x**2 )

area(45,pi = math.pi)


# # Challenge 2 - Splitting Strings
# 
# We have first looked at combining strings into one long string. There are times where we need to do the opposite and split the string into smaller components for further analysis. 
# 
# In the cell below, split the string into a list of strings using the space delimiter. Count the frequency of each word in the string in a dictionary. Strip the periods, line breaks and commas from the text. Make sure to remove empty strings from your dictionary.

# In[39]:


poem = """Some say the world will end in fire,
Some say in ice.
From what I’ve tasted of desire
I hold with those who favor fire.
But if it had to perish twice,
I think I know enough of hate
To say that for destruction ice
Is also great
And would suffice."""

# Your code here:
poem_strip = poem.replace("\n"," ").replace(".","").replace(",","")
word_list = poem_strip.split(" ")

dict={}
for word in word_list:
    dict.update({word:word_list.count(word)})
print(dict)


# In the cell below, find all the words that appear in the text and do not appear in the blacklist. You must parse the string but can choose any data structure you wish for the words that do not appear in the blacklist. Remove all non letter characters and convert all words to lower case.

# In[51]:


blacklist = ['and', 'as', 'an', 'a', 'the', 'in', 'it']

poem = """I was angry with my friend; 
I told my wrath, my wrath did end.
I was angry with my foe: 
I told it not, my wrath did grow. 

And I waterd it in fears,
Night & morning with my tears: 
And I sunned it with smiles,
And with soft deceitful wiles. 

And it grew both day and night. 
Till it bore an apple bright. 
And my foe beheld it shine,
And he knew that it was mine. 

And into my garden stole, 
When the night had veild the pole; 
In the morning glad I see; 
My foe outstretched beneath the tree."""

# Your code here:

poem2 = poem.lower()
charlist=[]
for word in poem2:
    for char in word:
        if not (char.isalpha()) and (char != " "):
            charlist.append(char)
charlist=set(charlist)
print(charlist) # liste des caracteres a enlever
for letter in poem2:
    if letter in charlist:
        newpoem = poem2.replace(letter,"")
        poem2 = newpoem
newpoem = newpoem.split(" ")  # we cleaned the code 
set1 = set(blacklist)
set2 = set(newpoem)
R = set2 - set1
print(R)


# In[ ]:





# In[ ]:




