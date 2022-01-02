#!/usr/bin/env python
# coding: utf-8

# # Kata 1

# In[1]:


#Count sheeps
T = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
True_l = T.count(True)
print(True_l)


# # Kata 2

# In[2]:


#Removing elements: Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.

#1st method:
Text = ["Keep", "Remove", "Keep", "Remove", "Keep"]
Text.remove ('Keep')
def remove_every_other(my_list):
    for i in range(0,len(my_list),2):
        print(my_list[i])
        
remove_every_other(Text)


# In[3]:


#2nd method:

Text = ["Keep", "Remove", "Keep", "Remove", "Keep"]
l=[]
x= "Keep"
while x in Text:
        Text.remove(x)
        
Text


# In[4]:


Text1 = ["Keep", "Remove", "Keep", "Remove", "Keep"]
def ffff(Text):

    f=True
    for i in range(len(Text)):
        if i%2 == 1 and f==True:
      
            Text.pop(i)
            f=False;
        elif i%2 == 0 and f==False:
            Text.pop(i)
            break
    print(Text)
        
ffff(Text1)
    
    


# In[5]:


Text = ["Keep", "Remove", "Keep", "Remove", "Keep"]
Text.pop(1)
        
Text


# # Katas 3

# In[6]:


#Convert number to reversed array of digits


#1st method
number = input("Input a number: ")
for char in range(len(number) - 1, -1, -1):
  print(number[char], end="")
print("\n")


# In[7]:


#2nd method

ll=[1,2,3]
ll.reverse()
ll


# # Katas 4

# In[ ]:


#Square
def squaring ():
    n=int(input("number of el"))
    for i in range (0, n):
        number =int(input("Input a number: "))
        number1=number**2
        print(number1)
squaring()


# 
# # Katas 5

# In[ ]:


#Count specific digits from a given list of integers
L1 =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
L2 = [1, 3]
L3 = []
for i in L1:
    L1.count[i]
    print(L3)

