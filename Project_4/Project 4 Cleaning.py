#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics Review

# 

# ## Context

# ![img](./diamonds.jpg)

# 
# The dataset we will be using is comprised of approximately 54k rows and 11 different columns. As always, a row represents a single observation (in this case a diamond) and each of the columns represent a different feature of a diamond.
# 
# The following codebook was provided together with the dataset to clarify what each column represents:
# 

# | Column  | Description  |
# |---|---|
# | Price  | Price in US dollars (326-18,823)  |
# | Carat  | Weight of the diamond (0.2--5.01)  |
# | Cut  | Quality of the cut (Fair, Good, Very Good, Premium, Ideal)  |
# | Color  | Diamond colour, from J (worst) to D (best)  |
# | Clarity  | A measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))   |
# | x  | Length in mm (0--10.74)  |
# | y  | Width in mm (0--58.9)  |
# | z  | Depth in mm (0--31.8)  |
# | Depth  | Total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)  |
# | Table  | Width of top of diamond relative to widest point (43--95)  |

# ## Libraries
# Pandas and numpy will be needed for the analysis of the data. 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# First import the data from the .csv file provided and assign it to a variable named `diamonds` and drop the column with the index.

# In[2]:


diamonds = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Projects\Project 4\diamonds.csv')
diamonds = diamonds.drop('Unnamed: 0', axis=1) #drop the column with the index called 'Unnamed: 0'


# # 1. Taking the first look at the data.
# Let's see how the data looks by using pandas methods like `head()`, `info()` and `describe()`. 
# 
# **First, use the `head` method.**

# In[3]:


#your code here
diamonds.head(5)


# In[4]:


diamonds.info()


# In[5]:


diamonds.describe()


# We can see the first 5 rows of the dataset using the `head` method. This by itself doesn't tell us much about the data that we have, but we can have a first look at the features (columns) and some of the values that each one takes.
# 
# **What do you see? Make some comments about the values you see in each column, comparing them with the codebook. Is that what you would expect for these variables?**
The data types are correct. However, we shouldn't have the minimum x=0 , y=0 and z=0 because we are working with physical objects.
# It is very important to know the amount of data we have, because everything will depend on that, from the quality of the analysis to the choice of our infrastracture.
# 
# **Check the shape of the data**

# In[6]:


#your code here
diamonds.shape


# The `clarity` column is confusing because we are not diamond experts. Let's create a new column with a new scale that is more understandable for us.
# 
# **Create a new column with numbers from 0 to 7. The lowest would be 0 with value `I1` and the greatest 7 with value `IF`**

# In[7]:


# create a list of our conditions for the column 'clarity'
conditions = [
    (diamonds['clarity'] == 'I1' ),
    (diamonds['clarity'] == 'SI2'),
    (diamonds['clarity'] == 'SI1'),
    (diamonds['clarity'] == 'VS2'),
    (diamonds['clarity'] == 'VS1'),
    (diamonds['clarity'] == 'VVS2'),
    (diamonds['clarity'] == 'VVS1'),
    (diamonds['clarity'] == 'IF')
    ]

# create a list of the values we want to assign for each condition
values = ['0', '1', '2', '3', '4', '5', '6' ,'7'] 

# create a new column and use np.select to assign values to it using our lists as arguments
diamonds['clarity_new'] = np.select(conditions, values)

# display updated DataFrame
diamonds.head()


# It makes sense to do the same with the `color` column.
# 
# **Do the same with values from 0 to 6. Read the codebook to see the match**

# In[8]:


#your code here
# create a list of our conditions for the column 'color'
conditions = [
    (diamonds['color'] == 'J'),
    (diamonds['color'] == 'I'),
    (diamonds['color'] == 'H'),
    (diamonds['color'] == 'G'),
    (diamonds['color'] == 'F'),
    (diamonds['color'] == 'E'),
    (diamonds['color'] == 'D')
    ]

# create a list of the values we want to assign for each condition
values = ['0', '1', '2', '3', '4', '5', '6'] 

# create a new column and use np.select to assign values to it using our lists as arguments
diamonds['color_new'] = np.select(conditions, values)

# display updated DataFrame
diamonds.head()


# With the `info` method, we can see the features of the dataset, and the amount of observations (rows) that have a non-null value and the types of the features. 
# 
# **Now use the `info` method and comparing with the shape, comment on what you see**

# In[9]:


#your code here
diamonds.info()

We have the same numbers of rows with 12 columns. Two additional columns compared to the original dataframe, the type is object for the new columns. The information method gives us the number of columns, the labels, data types, memory usage, range index, and the number of cells in each column.
# In the last line of the info output, you have some information about the types of the columns. As you know, it is a good idea to check if the types of each column is what you expect. If a column has the right type, we will be able to do all the operations that we want to do. 
# 
# For instance, if we have a column that is a `date` with a `string` format, we will have the data but we won't be able to do a simple operation, such as format the date the way that we would like.
# 
# Changing the data type to the one we needs can help us to solve a lot of problems in our data.
# 
# **Check the types of each column and comment if it matches with the expected**

# In[10]:


#your code here
diamonds.dtypes

The data types of each column are correct.
# # 2. A deeper look: checking the basic statistics.
# 
# The `describe` method gives us an overview of our data. From here we can see all the descriptive metrics for our variables.
# 
# **Use the `describe` method and comment on what you see**

# In[11]:


#your code and comments here
diamonds.describe()


# You have probably noticed that the columns x, y and z have a minimum value of 0. This means that there are one or more rows (or observations) in our dataset that are supposedly representing a diamond that has lenght, width or depth of 0. Considering that we're talking about a physical object, this is impossible!
# 
# Now let's proceed to check the rows that have a value of 0 in any of the x, y or z columns. By doing this we want to check if the data we are missing can be obtained using the data that we do have.
# 
# **Check the columns with `x`, `y` and `z` with value 0 in all of them and comment what you see**

# In[12]:


#your code here
#The number of 0 per column
print((diamonds['x'] == 0).sum())
print((diamonds['y'] == 0).sum())
print((diamonds['z'] == 0).sum())


# In[13]:


# 20 rows with 0 in column 'z'
diamonds.loc[diamonds['z'] == 0]


# In[14]:


# 12 rows with z as a missing value but we have x and y so we can calculate z
diamonds[(diamonds['x'] != 0 ) & (diamonds['y'] != 0) & (diamonds['z'] == 0)]


# In[15]:


# 8 rows with x as a missing value
diamonds.loc[diamonds['x'] == 0] 


# In[16]:


# 7 rows with y as a missing value
diamonds.loc[diamonds['y'] == 0] 


# In[17]:


# 7 rows - missing all 3 values 
diamonds[(diamonds['x'] == 0 ) & (diamonds['y'] == 0)]


# As you can see, we have 20 rows that have a value of 0 in some or all the aforementioned columns.
# Most of them (12) are missing the z value, which we can obtain using the columns depth, x and y. 
# 
# 20 rows with issues represent just 0.03% of our data (20 out of 53940) so it wouldn't be a big deal to remove them. Still, lets try to keep all the data we have. 
# 
# For those 12 rows, we will create a function that applies the formula given in the codebook and get the value of z. We will drop the other rows (8), since they are missing all 3 values or 2 of them.
# 
# **Create a function named `calculate_z` that applies the function in the codebook to one single row you give to the function**

# In[18]:


#your code here

def calculate_z(a,b,depth):
    per_depth = depth /100
    m = ((a + b)/2) * per_depth
    return m
 

# If we want to the first value of z:
#calculate_z(diamonds["x"][0],diamonds["y"][0],diamonds["depth"][0]) 

#If we remove the indexes, we are going to find z for for all column: calculate_z(diamonds["x"],diamonds["y"],diamonds["depth"])
#However, in some cases z is going to be false where we are missing x or y - it`s going to make calculation with x = 0 and y = 0 but it`s not possible


#calcul z for the 12 rows
indexes=[2207, 2314, 4791,5471,10167,13601,24394,26123,27112,27503,27739,51506]
for index in indexes:
    diamonds.z[index] = calculate_z(diamonds["x"][index],diamonds["y"][index],diamonds["depth"][index])




# In[19]:


# 8 rows with z as missing value
(diamonds['z'] == 0).sum()


# **Apply it just to the rows with incorrect values**

# If we leave the other 8 values as they are, it would negatively affect our analysis, because these are data that do not make logical sense. Therefore it is better to consider those values as NaN values, since they are probably the result of a mistake or error during process of measuring and storing these values in a dataset.
# 
# To replace them we can use the pandas .replace() method and np.NaN.
# 
# **Replace the zero values in the `z` column for a NaN**

# In[20]:


#your code here
diamonds = diamonds.replace(0, np.nan)


# In[21]:


# Verify if we still have rows with z = 0
print((diamonds['z'] == 0).sum())


# ----
# # Bonus: check the new z values
# Since we need to be 100% sure of our data, let's create a function that validates our z. To do so, we will use the same formula, but this time we will calculate the value of depth with the new value assigned to z.
# 
# **Create a function named `validate_z` that compares the `z`  in cells above with the one thrown by the formula and run it with the rows you changed in the cells above**

# In[22]:


#your code here
def validate_z(i):
    z=diamonds['depth'][i]*((diamonds['x'][i])+(diamonds['y'][i]))/(2*100)
    return z

#find the index of rows to fix
condition_z = (diamonds['z']==0) & (diamonds['y']!=0) & (diamonds['x']!=0)
in_to_fun_lambda = diamonds.loc[lambda x: condition_z==True].index.tolist()
in_to_fun_lambda
for i in in_to_fun_lambda:
    x=(calculate_z(i))
    diamonds.at[i,'z']=x
    


# In[23]:


diamonds.describe()


# Let's check the data again with the `describe()` method.

# The minimum value for x, y and z should now be a positive number, as it should be for the physical measurements of an object.

# Let's finish by checking for NaN values in the data. Since we introduced them ourselves using 'replace', we will surely find some, but there may be more that are unrelated to the x, y and z columns. Checking NaNs is a fundamental part of data cleaning and it's always better to do this kind of operations before proceeding with analysis.
# 
# **Check how many NaNs do you have, comment what you would do with those values, and then do so**

# In[24]:


#your code here
diamonds.isnull().sum()


# In[ ]:


#your comments here
8 non values in column x so we can't calculate 8 z. It doesn't bring us any information.


# # 3. Checking for outliers
# Now we are going to revisit the summary table to check for outliers.
# 
# **Use the `describe` method again and comment on what you see. After that, check if you have any outliers** 

# In[25]:


#your code here
diamonds.describe()


# In[ ]:


#your comments here
There is a big gap between the less expensive product and the most expensive product. The mean is higher than the median, our data is right skewed. 
This means that there are a few outliers that influence the mean and cause the data to be skewed.


# To manage these outliers, we are going to filter our DataFrame, we're going to take all the values that have a price higher than the 75th percentile.
# 
# **Look for that quantile and filter the dataframe to clearly see the outliers. What do you think?**

# In[26]:


#your code here
diamonds[diamonds["price"] >diamonds["price"].quantile(.75)]


# Our dataset is really big and the outliers are really far apart from the rest of the values. To see this more clearly we will use a boxplot, which plots the median, 25th and 75th quartile, the maximum and minimum, as well as any outliers.

# In[27]:


#Run this code
fig, ax = plt.subplots(1,2, figsize=(10, 5))
sns.boxplot(y=diamonds.y, ax=ax[0])
sns.boxplot(y=diamonds.z, ax=ax[1])
plt.subplots_adjust(wspace=0.5)


# Now we can see that all the values are within an acceptable range, but we have 2 big outliers in y and 1 in z. Now we know that our max values for y should be around 10 and the values for z should be around 6, so let's filter our dataset to find values higher than 10 in it.
# 

# In[28]:


#your code here
diamonds[diamonds['z']>10]


# Now that we have found the outlier, let's use the function we defined earlier to correct this value. First, we need to change the value to 0 (because that's how we defined the function before) and then we will apply it.
# 
# **Apply `calculate_z` for the row with the outlier**

# In[29]:


# Find the index where z > 10
print(np.where(diamonds['z']>10))


# In[30]:


#your code here
calculate_z(diamonds["x"][48410],diamonds["y"][48410],diamonds["depth"][48410]) 


# Let's check if we actually corrected the outlier.

# In[31]:


diamonds.loc[48410]


# Cool! Now let's validate our new `z`. We will check if we obtain the same value of depth using our validate function. If the formula applies, this means could approximate the real value of `z`.
# 
# **Apply `validate_z` to the row used earlier**

# In[34]:


#your code here
validate_z(diamonds['depth'][48410]*((diamonds['x'][48410])+(diamonds['y'][48410]))/(2*100))


# Now let's do the same for `y`. First, let's filter the DataFrame to find the outliers. We said that the maximum values should be around 10, so let's check what are the values above 10.
# 
# **Check the values greater than 10 in the `y` column** 

# In[33]:


#your code here
diamonds[diamonds['y']>10]


# We can clearly see that the 31.8 in row 49189 is an outlier for the y value. Also, we can see that the 58.9 value for `y` in row 24067 is actually its depth, so it was a mistake when they introduced the data. Let's create a function to fix these outliers.
# 
# **Create a function named `calculate_y` to calculate `y` using `z` and `x` the same way you did above**

# In[ ]:


#your code here
def calculate_y(a,b,depth):
    


# We will check the rows that had an outlier in `y`, to check that the values were changed.
# 
# **Check those rows (also validating with your function) and comment what you see**

# Now that we have corrected or dropped all of our outliers, lets plot another box plot to double check.

# In[35]:


#Run this code
fig, ax = plt.subplots(1,2, figsize=(10, 5))
sns.boxplot(y=diamonds.y, ax=ax[0])
sns.boxplot(y=diamonds.z, ax=ax[1])
plt.subplots_adjust(wspace=0.5)


# **What do you think? Are these values more reasonable?**
# 

# In[ ]:


#your thoughts here


# **Once you are happy with your cleaning, save the cleaned data and continue to csv. Your new csv should be named ``diamonds_clean``**

# In[37]:


#your code here
# Export data
diamonds.to_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Projects\Project 4\diamonds_clean.csv', index=False)

