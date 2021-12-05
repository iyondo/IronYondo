#!/usr/bin/env python
# coding: utf-8

# # [Rr]eg[Ee]xp? Lab
# 
# # Challenge 1- Regular Expressions
# 
# Sometimes, we would like to perform more complex manipulations of our string. This is where regular expressions come in handy. In the cell below, return all characters that are upper case from the string specified below.

# In[6]:


import re

poem = """The apparition of these faces in the crowd;
Petals on a wet, black bough."""

# Your code here:

pattern = r"[A-Z]"
re.findall(pattern, poem)


# In the cell below, filter the list provided and return all elements of the list containing a number. To filter the list, use the `re.search` function. Check if the function does not return `None`. You can read more about the `re.search` function [here](https://docs.python.org/3/library/re.html).

# In[9]:


import re
data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']
# Your code here:
t= " ".join(data)
p="[\d]"
re.search(p, t)


# # Challenge 2 - Regular Expressions II
# 
# In the cell below, filter the list provided to keep only strings containing at least one digit and at least one lower case letter. As in the previous question, use the `re.search` function and check that the result is not `None`.
# 
# To read more about regular expressions, check out [this link](https://developers.google.com/edu/python/regular-expressions).

# In[ ]:


data = ['123abc', 'abc123', 'JohnSmith1', 'ABBY4', 'JANE']
# Your code here:


# # Challenge 3 -  Advanced Regular Expressions
# 
# Complete the following set of exercises to solidify your knowledge of regular expressions.

# In[ ]:


import re


# ### 1. Use a regular expression to find and extract all vowels in the following text.

# In[14]:


import re
text = "This is going to be a sentence with a good number of vowels in it."
r = re.findall("[a,e,i,o,u,y]",  text)
print(r)

        
     


# ### 2. Use a regular expression to find and extract all occurrences and tenses (singular and plural) of the word "puppy" in the text below.

# In[ ]:


text = "The puppy saw all the rest of the puppies playing and wanted to join them. I saw this and wanted a puppy of my own!"


# In[16]:


import re
text = "The puppy saw all the rest of the puppies playing and wanted to join them. I saw this and wanted a puppy of my own!"
r = re.findall("puppy|puppies", text)
print(r)


# ### 3. Use a regular expression to find and extract all tenses (present and past) of the word "run" in the text below.

# In[17]:


text = "I ran the relay race the only way I knew how to run it."


# In[18]:


import re
text = "I ran the relay race the only way I knew how to run it."
r = re.findall("ran|run", text)
print(r)


# ### 4. Use a regular expression to find and extract all words that begin with the letter "r" from the previous text.

# In[20]:


import re
text = "I ran the relay race the only way I knew how to run it."
r = re.findall("r[a-z]*", text)
print(r)


# In[48]:


# Solution
import re
text = "I ran the relay race the only way I knew how to run it."
print(re.findall(r"r[a-z]*", text))


# ### 5. Use a regular expression to find and substitute the letter "i" for the exclamation marks in the text below.

# In[ ]:


text = "Th!s !s a sentence w!th spec!al characters !n !t."


# In[22]:


import re
text =  "Th!s !s a sentence w!th spec!al characters !n !t."
r = re.sub("!", "i", text)
print(r)


# ### 6. Use a regular expression to find and extract words longer than 4 characters in the text below.

# In[ ]:


text = "This sentence has words of varying lengths."


# In[29]:


import re
text =  "This sentence has words of varying lengths."
r = re.findall("[a-z]{4,}", text)
print(r)


# In[49]:


#Solution
import re
text =  "This sentence has words of varying lengths."
print(re.findall(r"[a-z]{4,}", text))


# ### 7. Use a regular expression to find and extract all occurrences of the letter "b", some letter(s), and then the letter "t" in the sentence below.

# In[ ]:


text = "I bet the robot couldn't beat the other bot with a bat, but instead it bit me."


# In[35]:


import re
text = "I bet the robot couldn't beat the other bot with a bat, but instead it bit me."
r = re.findall("b[a-z]*t", text)
print(r)


# In[51]:


import re
text = "I bet the robot couldn't beat the other bot with a bat, but instead it bit me."
print(re.findall(r"b[a-z]*t", text))


# ### 8. Use a regular expression to find and extract all words that contain either "ea" or "eo" in them.

# In[ ]:


text = "During many of the peaks and troughs of history, the people living it didn't fully realize what was unfolding. But we all know we're navigating breathtaking history: Nearly every day could be — maybe will be — a book."


# In[57]:


import re
text = "During many of the peaks and troughs of history, the people living it didn't fully realize what was unfolding. But we all know we're navigating breathtaking history: Nearly every day could be — maybe will be — a book."
r = text.lower()
r1 = re.findall("[a-z]*ea[a-z]*", r) + re.findall("[a-z]*eo[a-z]*", r)
print(r1)


# In[52]:


#Solution
text = "During many of the peaks and troughs of history, the people living it didn't fully realize what was unfolding. But we all know we're navigating breathtaking history: Nearly every day could be — maybe will be — a book."
pattern = r"[a-z]*e[ao][a-z]*"
re.findall(pattern,text.lower())


# ### 9. Use a regular expression to find and extract all the capitalized words in the text below individually.

# In[ ]:


text = "Teddy Roosevelt and Abraham Lincoln walk into a bar."


# In[62]:


import re
text = "Teddy Roosevelt and Abraham Lincoln walk into a bar."
r = re.findall(r"[A-Z][a-z]*", text)
print(r)


# In[66]:


#Solution
pattern = r"[A-Z][a-z]*"
for word in re.findall(pattern,text):
    print(word)


# ### 10. Use a regular expression to find and extract all the sets of consecutive capitalized words in the text above.

# In[69]:


import re
text = "Teddy Roosevelt and Abraham Lincoln walk into a bar."
r = re.findall(r"[A-Z][a-z]* [A-Z][a-z]*", text)
print(r)


# In[70]:


#Solution
pattern = r"[A-Z][a-z]* [A-Z][a-z]*"
for set_words in re.findall(pattern,text):
    print(set_words)


# ### 11. Use a regular expression to find and extract all the quotes from the text below.
# 
# *Hint: This one is a little more complex than the single quote example in the lesson because there are multiple quotes in the text.*

# In[ ]:


text = 'Roosevelt says to Lincoln, "I will bet you $50 I can get the bartender to give me a free drink." Lincoln says, "I am in!"'


# In[74]:


import re
text = 'Roosevelt says to Lincoln, "I will bet you $50 I can get the bartender to give me a free drink." Lincoln says, "I am in!"'
r = re.findall(r"[a-z][A-z]*\n[a-z][A-z]*", text)
print(r)


# In[82]:


#Solution
import re
pattern = r'".+?"'
text = 'Roosevelt says to Lincoln, "I will bet you $50 I can get the bartender to give me a free drink." Lincoln says, "I am in!"'
re.findall(pattern,text)


# ### 12. Use a regular expression to find and extract all the numbers from the text below.

# In[ ]:


text = "There were 30 students in the class. Of the 30 students, 14 were male and 16 were female. Only 10 students got A's on the exam."


# In[85]:


import re 
text = "There were 30 students in the class. Of the 30 students, 14 were male and 16 were female. Only 10 students got A's on the exam."
r = "[0-9]+"
print(re.findall(r, text))


# ### 13. Use a regular expression to find and extract all the social security numbers from the text below.

# In[ ]:


text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""


# In[98]:


import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
r = re.findall(" \d+", text)
print(r)


# In[99]:


#Solution
import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
pattern = r"\d{3}-\d{2}-\d{4}"
re.findall(pattern,text)


# ### 14. Use a regular expression to find and extract all the phone numbers from the text below.

# In[109]:


import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
pattern = r".\d{3}.\d{3}-\d{4}" # les points font les parantheses
re.findall(pattern,text)


# In[104]:


#Solution
import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
pattern = r".\d{3}.\d{3}.\d{4}"
re.findall(pattern,text)


# ### 15. Use a regular expression to find and extract all the formatted numbers (both social security and phone) from the text below.

# In[119]:


import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
pattern1 = r".\d{3}.\d{3}.\d{4}" 
pattern2 = r"\d{3}-\d{2}-\d{4}"
print(re.findall(pattern1,text) + re.findall(pattern2,text))


# In[120]:


#Solution
import re
text = """
Henry's social security number is 876-93-2289 and his phone number is (847)789-0984.
Darlene's social security number is 098-32-5295 and her phone number is (987)222-0901.
"""
pattern = r".\d+.\d+.\d+"
re.findall(pattern,text)

