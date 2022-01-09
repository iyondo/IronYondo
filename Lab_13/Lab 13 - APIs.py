#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests


# # Challenge 1

# In[2]:


#Let's make an API call with the get method 
response = requests.get('https://xkcd.com/')
response


# In[3]:


#check the headers
response.headers


# In[4]:


#check the headers "Expires" value
response.headers['Expires']


# In[7]:


#Provide all HTML codes
response.content


# In[10]:


#Save the image via API with the get method
receive= requests.get("https://imgs.xkcd.com/comics/collections.png")
with open (r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 13\image.png','wb') as f: #the folder
    f.write(receive.content)


# # Challenge 2

# In[11]:


response_1 = requests.get('https://httpbin.org/get')
response_1


# In[16]:


#View url
response_1.url


# In[17]:


#Add parameters to the request 'things':2,'total':25
response_1={'things':2,'total':25}
response_1=requests.get('https://httpbin.org/get',params=response_1)
response_1


# In[19]:


#Add username and password as parameters
response_1={'Username':'Ingrid','Password':'Iron'}
r=requests.post('https://httpbin.org/post',data=response_1) #we use requests.post so it will appear
print(r.text)


# In[20]:


#Export username and password as dictionary
#send information to the website => so use 'post'
response_1={'Username':'manu','Password':'adm'}
r=requests.post('https://httpbin.org/post',data=response_1)
r_dict= r.json()
print(r_dict['form'])


# # Challenge 3

# In[21]:


response_3 = requests.get('https://github.com/ironhack-datalabs/scavenger')
results = response_3.json()
results

