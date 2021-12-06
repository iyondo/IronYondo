#!/usr/bin/env python
# coding: utf-8

# # Conditional Statements
# 
# Complete the following set of exercises to solidify your knowledge for Conditional Statements.

# #### 1. Write a Python program to find those numbers which are divisible by 3 and are between 1000 and 2500 (both included).

# In[30]:


x = int(input("Enter a number : "))
for i in range(1000, 2500):
        if i%3==0:
            print(i)


# In[35]:


# Solution
new=[]
for x in range(1000, 2500):
    if (x%3==0):
        new.append(str(x))
print (','.join(new))


# #### 2. Write a Python program to convert month name to a number of days in this months.

# In[57]:


x = str(input("Enter a month : "))
if x == "Janvier":
    print(31)
elif x == "Fevrier":
    print(29)
elif x == "Mars":
    print(31)
elif x == "Avril":
    print(30)
elif x == "Mai":
    print(31)
elif x == "Juin":
    print(30)
elif x == "Juillet":
    print(31)
elif x == "Aout":
    print(31)
elif x == "Septembre":
    print(30)
elif x == "Octobre":
    print(31)
elif x == "Novembre":
    print(30)
elif x == "Decembre":
    print(31)
else:
    print ("Please enter again: ")
    


# In[16]:


# 2e methode - Dictionnary
x = str(input("Enter a month : "))
months = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
number = ["31" , "29", "31", "30", "31" , "30" , "31" ,"31" , "30" , "31", "30" , "31"]
dictionnary = dict(zip(months, number))
print(dictionnary)
dict = {}
for i in range(11) :
    dict[[months[i]] == number[i]
print(i)
    


# #### 3. Write a Python program that accepts a word from the user and reverse it.

# In[1]:


word = input("Input a word to reverse: ")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# #### 4. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Iron" instead of the number and for the multiples of five print "Hack". For numbers which are multiples of both three and five print "Ironhack".

# In[19]:


for i in range(51):
    if i%3 == 0:
        print("Iron")
    elif  i%5 ==0:
        print("Hack")
    elif i%3 ==0 and i%5 ==0:
        print("IronHack")
    else:
        print("Else")


# #### 5.  A leap year is a calendar year containing an additional day added to keep the calendar year synchronized with the astronomical or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28. These extra days occur in years which are multiples of four (with the exception of centennial years not divisible by 400). Write a Python program, which asks for a year and calculates, if this year is a leap year or not.

# In[22]:


x = int(input("Enter a year: "))
if x %4 == 0:
    print("It's a lap year")
else:
    print("It's not a lap year")


# #### 6. Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is universally expressed in units of kg/m2, resulting from mass in kilograms and height in metres. Write a program, which asks for the length and the weight of a person and returns an evaluation string according to the following table:
# ![image.png](attachment:image.png)

# In[28]:


x = int(input("Enter your weight: "))
y = int(input("Enter your height: "))
if (x/y**2)>0 and (x/y**2)<15:
    print("Very severely underweight")
elif (x/y**2)>15 and (x/y**2)<16:
    print("Severely underweight")
elif (x/y**2)>16 and (x/y**2)<18.5:
    print("Underweight")
elif (x/y**2)>18.5 and (x/y**2)<25:
    print("Normal")
elif (x/y**2)>25 and (x/y**2)<30:
    print("Overweight")
elif (x/y**2)>30 and (x/y**2)<35:
    print("Obese Class I (Moderately obese)")
elif (x/y**2)>35 and (x/y**2)<40:
    print("Obese Class II (Severely obese)")
elif (x/y**2)>40 and (x/y**2)<45:
    print("Obese Class III (Morbidy Obese)")
elif (x/y**2)>45 and  (x/y**2)<50:
    print("Obese Class IV (Super Obese)")
elif (x/y**2)>50 and (x/y**2)<60:
    print("Obese Class V (Super Obese)")
else:
    print("Obese Class VI (Hyper Obese)")


# ### Bonus

# https://realpython.com/python-conditional-statements/
