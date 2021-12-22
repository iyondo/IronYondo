#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# # Challenge 2 - Working with JSON files
# 
# Import the pandas library.

# In[33]:


# your code here
import pandas as pd


# In the next cell, load the data in `nasa.json` in the `data` folder and load it into a pandas dataframe. Name the dataframe `nasa`.

# In[18]:


# your code here
nasa = pd.read_json(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\nasa.json', orient = 'columns') #orient = 'columns' is not mandatory
nasa


# In[ ]:


# 2e methode:
#import json
# with open(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\nasa.json') as f:
#data = json.load(f)
#data


# In[ ]:


#Dataframe
#nasa = pd.DataFrame(data)
#print(nasa)


# Now that we have loaded the data, let's examine it using the `head()` function.

# In[13]:


# your code here
nasa.head()


# In[14]:


#columns
nasa.columns


# #### The `value_counts()` function is commonly used in pandas to find the frequency of every value in a column.
# 
# In the cell below, use the `value_counts()` function to determine the frequency of all types of asteroid landings by applying the function to the `fall` column.

# In[15]:


# your code here
nasa.fall.value_counts()
#Fell     996
#Found      4


# Finally, let's save the dataframe as a json file again. Save the dataframe using the `orient=records` argument and name the file `nasa-output.json`. Remember to save the file inside the `data` folder.

# In[16]:


# your code here
nasa.to_json(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\nasachange.json', orient='records')


# In[19]:


#Check all the first column
nasa.iloc[:,0:1] # 


# # Challenge 2 - Working with CSV and Other Separated Files
# 
# CSV files are more commonly used as dataframes. In the cell below, load the file from the URL provided using the `read_csv()` function in pandas. Starting version 0.19 of pandas, you can load a CSV file into a dataframe directly from a URL without having to load the file first and then transform it. The dataset we will be using contains information about NASA shuttles.
# 
# In the cell below, we define the column names and the URL of the data. Following this cell, read the tst file to a variable called `shuttle`. Since the file does not contain the column names, you must add them yourself using the column names declared in `cols` using the `names` argument. Additionally, a tst file is space separated, make sure you pass ` sep=' '` to the function.

# In[20]:


cols = ['time', 'rad_flow', 'fpv_close', 'fpv_open', 'high', 'bypass', 'bpv_close', 'bpv_open', 'class','new' ] #1 name added for the 10th column
tst_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst'


# In[23]:


# your code here
shuttle = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst', sep=' ')
shuttle


# In[24]:


#Not possible to add the names to the columns: axis has 10 elements, new values have 9 elements
shuttle.columns = cols
shuttle


# Let's verify that this worked by looking at the `head()` function.

# In[25]:


# your code here
shuttle.head()


# To make life easier for us, let's turn this dataframe into a comma separated file by saving it using the `to_csv()` function. Save `shuttle` into the file `shuttle.csv` and ensure the file is comma separated, that we are not saving the index column and that the file is saved inside the `data` folder.

# In[26]:


# your code here
# Export comma-separated variable file
shuttle.to_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\shuttle.csv', index=False)


# # Challenge 3 - Working with Excel Files
# 
# We can also use pandas to convert excel spreadsheets to dataframes. Let's use the `read_excel()` function. In this case, `astronauts.xls` is in the `data` folder. Read this file into a variable called `astronaut`. 
# 
# Note: Make sure to install the `xlrd` library if it is not yet installed.

# In[34]:


# your code here
import xlrd


# In[35]:


astronaut = pd.read_excel(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\astronauts.xls')
astronaut


# Use the `head()` function to inspect the dataframe.

# In[36]:


# your code here
astronaut.head()


# In[30]:


#columns
astronaut.columns


# Use the `value_counts()` function to find the most popular undergraduate major among all astronauts.

# In[38]:


astronaut['Undergraduate Major'].value_counts()  # on utilise les crochets car il y'a un espace


# In[37]:


# 2nd method: change the column name to Undergraduate_Major to avoid any space
#astronaut.rename(columns={'Undergraduate Major': 'Undergraduate_Major'})
#astronaut.Undergraduate_Major.value_counts() 


# Due to all the commas present in the cells of this file, let's save it as a tab separated csv file. In the cell below, save `astronaut` as a **tab separated file** using the `to_csv` function. Call the file `astronaut.csv`. Remember to remove the index column and save the file in the `data` folder.

# In[ ]:


# your code here
astronaut.to_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\astronaut.csv', index=False)


# # Bonus Challenge - Fertility Dataset
# 
# Visit the following [URL](https://archive.ics.uci.edu/ml/datasets/Fertility) and retrieve the dataset as well as the column headers. Determine the correct separator and read the file into a variable called `fertility`. Examine the dataframe using the `head()` function. 
# 
# Look in Google for a way to retrieve this data!

# In[ ]:


# your code here
#fertility = pd.read_csv('https://archive.ics.uci.edu/ml/datasets/Fertility', sep=' ')
#fertility


# In[8]:


fertility = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 1\Lab 28\fertility_Diagnosis.txt')
fertility


# In[ ]:




