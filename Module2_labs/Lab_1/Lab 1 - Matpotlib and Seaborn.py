#!/usr/bin/env python
# coding: utf-8

# # Lab | Matplotlib & Seaborn
# 
# #### Import all the necessary libraries here:

# In[2]:


# Libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt   
import pandas as pd
import seaborn as sns
import numpy as np


# ## Challenge 1
# 
# #### The data we will use in this challenge is:

# In[3]:


x = np.arange(0,100)
y = x*2
z = x**2


# #### Plot (x, y) and (x, z).
# There are 2 ways of doing this. Do in both ways.
# 
# **Hint**: Check out the nrows, ncols and index arguments of subplots. 
# 
# Also, play around with the linewidth and style. Use the ones you're most happy with.

# In[6]:


#1st method

plt.figure

# Plot 1
plt.subplot(1,2,1)
plt.plot(x, y)

# Plot 2
plt.subplot(1,2,2)
plt.plot(x, z)

# Show the plot
plt.show()


# #### Use plt.subplots(nrows=1, ncols=2) to create the plot.

# In[11]:


# Method 2 - We have the same scale

fig, [ax1, ax2] = plt.subplots(1,2)

# Plot 1
ax1.plot(x,y)
   
   
# Plot 2
ax2.plot(x,z)


# Show the plot
plt.show()


# #### Use your previous code but now, resize your plot.
# **Hint**: Add the figsize argument in plt.subplots().
# 
# If you want, try to add a title to the plot or even axes labels. You can also play with the fontweight and fontsize of the titles and labels. 

# In[23]:


# your code here

fig, [ax1, ax2] = plt.subplots(1,2,figsize=(10, 5)) #figsize spécifie la largeur et la hauteur de la figure en pouces


# Plot 1
ax1.plot(x,y)
ax1.set_title('Plot1')   
ax1.set_xlabel('x label')     
ax1.set_ylabel('y label')   


# Plot 2

ax2.plot(x,z)
ax2.set_title('Plot2')   
ax2.set_xlabel('x label')     
ax2.set_ylabel('z label')   



plt.show()


# In[35]:


# your code here


fig, [ax1, ax2] = plt.subplots(1,2,figsize=(10, 5)) #figsize spécifie la largeur et la hauteur de la figure en pouces


# Plot 1
ax1.plot(x,y)
ax1.set_title('Plot1', fontsize = 25)   
ax1.set_xlabel('x label', fontsize = 50)     
ax1.set_ylabel('y label', fontsize = 50)   


# Plot 2

ax2.plot(x,z)
ax2.set_title('Plot2', fontsize = 35, fontweight = 'bold')    #fontweight si c'Est gras etc... 
ax2.set_xlabel('x label', fontsize = 10)     
ax2.set_ylabel('z label', fontsize = 10)   



plt.show()



# #### Now you will have to plot both $y=x^2$ and $y=e^x$ in the same plot. Create two subplots and use a normal scale in the first one and a logarithmic scale in the second one.
# **Hint**: Use `set_xscale` and `set_yscale`.

# In[43]:


# your code here
y=x**2
y = np.exp(x)


# In[56]:




fig, [ax1, ax2] = plt.subplots(1,2)


#plot 1
ax1.plot(y, x**2)
ax1.set_title('Plot1')   
ax1.set_xlabel('x label')     
ax1.set_ylabel('y label') 
ax1.set_xscale('linear')


# Plot 2
ax2.plot(y, np.exp(x))
ax2.set_title('Plot2')   
ax2.set_xlabel('x label')     
ax2.set_ylabel('z label') 
ax2.set_yscale('log')

plt.legend([ax1, ax2],['x**2', 'np.exp(x)'])


# In[16]:


# Create a figure of a fixed size and axes
f, ax = plt.subplots(1, 2, figsize=(10,4))

# Normal plot
ax[0].plot(x, x**2, 'r', x, np.exp(x), 'g')  #r for color red and g for color green
ax[0].set_title("Normal scale")

# Logarithmic scale
ax[1].plot(x, x**2, "r", x, np.exp(x), 'g')
ax[1].set_yscale("log")
ax[1].set_title("Logarithmic scale (y)")


# Show plot
plt.show()


# #### As a bonus challenge, try to add a legend to the plot.

# In[10]:


# your code here
# ALTERNATIVE WITH LEGEND
# Create a figure of a fixed size and axes
f, ax = plt.subplots(1, 2, figsize=(10,4))

# Normal plot
ax[0].plot(x, x**2, 'r', label = 'x**2')
ax[0].plot(x, np.exp(x), 'g', label = 'exp(x)')
ax[0].set_title("Normal scale")
ax[0].legend()

# Logarithmic scale
ax[1].plot(x, x**2, 'r', label = 'x**2')
ax[1].plot(x, np.exp(x), 'g', label = 'exp(x)')
ax[1].set_yscale("log")
ax[1].set_title("Logarithmic scale (y)")
ax[1].legend()

# Show plot
plt.show()


# ## Challenge 2
# #### Import the `Fitbit2` dataset and store it in a variable called `fitbit`. You can find the dataset in Ironhack's database:
# * db: `fitbit`
# * table: `fitbit2`

# In[11]:


# your code here
fitbit = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Lab 1\Fitbit2.csv')
fitbit


# In[12]:


fitbit.columns


# #### From the Fitbit data, we want to visually understand:
# 
# How the average number of steps change by month. Use the appropriate visualization to show the median steps by month. Is Fitbitter more active on weekend or workdays? All plots must be in the same jupyter notebook cell.
# 
# **Hints**:
# 
# * Use Months_encoded and Week_or Weekend columns.
# * Use matplolib.pyplot object oriented API.
# * Set your size figure to 12,4
# * Explore plt.sca
# * Explore plt.xticks
# * Save your figures in a folder called `figures` in your repo. 

# In[18]:


# MEDIAN STEPS BY MONTH_ENCODED
# Find the median steps for each month
weekday_steps = fitbit['Steps'].groupby(fitbit['Months_encoded']).median()


# Create a figure of a fixed size and axes = 1st graph
f, ax = plt.subplots(1,2, figsize = (12,4))

# Set the current axes instance to ax[0] - Now plt methods will affect ax[0]
plt.sca(ax[0]) # we can have it on the same scale

# Plot the weekday steps in the current axes
weekday_steps.plot(kind = 'line',linewidth=2)

# Add labels, title, etc
plt.ylabel('Median number of steps')
plt.xlabel('Months')
plt.title('Median Steps walked by month')
plt.xticks(range(13), ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

# Save the figure
plt.savefig(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Lab 1\figures\steps_months.png',bbox_inches='tight')




# MEDIAN STEPS BY WORK_OR_WEEKEND = 2nd graph
# Set the current axes instance to ax[1] - Now plt methods will affect ax[1]
plt.sca(ax[1])

# Find the median steps for workdays and weekdays
weekday_steps = fitbit['Steps'].groupby(fitbit['Work_or_Weekend']).median().sort_values()

# Plot the workday and weekend steps in the current axes
weekday_steps.plot(kind = 'bar', alpha = 0.5)

# Add labels, title, etc
plt.ylabel('Median number of steps')
plt.title('Median Steps walked by Workdays and Weekend')
plt.xticks(range(2), ['Weekend','Workdays'], rotation = 0)

# Save the figure
plt.savefig(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Lab 1\figures\steps_work_weekend.png', bbox_inches='tight')


# #### Write a loop to plot 3 scatter plots of the following features:
# 
# * Minutes Lightly Active vs Steps    
# * Minutes Very Active vs Steps    
# * Minutes Sedentary vs Steps  

# In[19]:


# your code here
# ALTERNATIVE 1
# Create a df with the columns we are interested in 
cols = ['Minutes Lightly Active','Minutes Very Active','Minutes Sedentary','Steps']
df = fitbit[cols]

# Create a figure of a fixed size and axes
f, ax = plt.subplots(1, 3, figsize = (20,8))

# Iterate to draw each scatter plot
for i in range(3):
    plt.sca(ax[i])
    plt.scatter(df[cols[i]], df[cols[3]], color = 'darkblue')
    plt.xlabel(df[cols[i]].name)
    plt.ylabel('Steps')


# In[20]:


# ALTERNATIVE 2
# Create a df with the columns we are interested in 
cols = ['Minutes Lightly Active','Minutes Very Active','Minutes Sedentary','Steps']
df = fitbit[cols]

# Create a figure of a fixed size and axes
f, ax = plt.subplots(1, 3, figsize = (20,8))

# Iterate to draw each scatter plot
for i in range(3):
    ax[i].scatter(df[cols[i]], df[cols[3]], color = 'darkblue')
    ax[i].set_xlabel(df[cols[i]].name)
    ax[i].set_ylabel('Steps')


# ## Challenge 3
# 
# #### Import the `titanic` dataset and store it in a variable called `titanic`. You can find the dataset in Ironhack's database:
# * db: `titanic`
# * table: `titanic`

# In[21]:


# your code here
titanic = pd.read_csv(r'C:\Users\Ingrid\Desktop\DAFT Nov 21\Labs done\Labs module 2\Lab 1\titanic.csv')


# #### Explore the titanic dataset using Pandas dtypes.

# In[22]:


# your code here
titanic.dtypes


# #### What are your numerical variables? What are your categorical variables?
# **Hint**: Use Pandas select_dtypes.

# In[24]:


# NUMERICAL VARIABLES
# your code here
titanic.select_dtypes(include=['float64','int64']).dtypes

#Alternative: titanic.select_dtypes(exclude=object).dtypes


# In[25]:


# CATEGORICAL VARIABLES
# your code here
titanic.select_dtypes(include=['object']).dtypes

#Alternative: titanic.select_dtypes(exclude=['int','float']).dtypes


# #### Set the plot style to classic and the figure size to (12,6).
# **Hint**: To set the style you can use matplotlib or seaborn functions. Do some research on the matter.

# In[26]:


# your code here
# Plot style change
plt.style.use('classic')   # matplotlib
sns.set_style('whitegrid') # seaborn

# Figure size change
plt.rcParams['figure.figsize'] = (12, 6)


# #### Use the right visulalization to show the distribution of column `Age`.

# In[27]:


# your code here
# Pandas plots are based on matplotlib

# Plot the histogram of column Age
titanic['Age'].hist(bins=50)

# Set titles, labels, etc
plt.title('Distribution of age')
plt.xlabel('Age')
plt.ylabel('Count')

# Show the plot
plt.show()


# #### Use subplots and plot the distribution of the `Age`  with bins equal to 10, 20 and 50.

# In[28]:


# Variables
bins = [10, 20, 50]

# Create a figure of a fixed size and axes
f, ax = plt.subplots(1,3) #3 bins
f.set_figwidth(15)

# Plot the histogram using a different number of bins
for i in range(3):
    plt.sca(ax[i])
    titanic['Age'].hist(bins=bins[i])
    plt.title('n =' + str(bins[i]))
    plt.xlabel('Age')
    plt.ylabel('Count')


# #### How does the bin size affect your plot?

# In[ ]:


"""
your comments here
"""
Using a low number of bins (wider bins) reduces noise on the distribution estimation while using a 
high number of bins (narrower bins) gives greater precision to the distribution estimation (and more noise). 


# #### Use seaborn to show the distribution of column `Age`.

# In[29]:


# your code here

# Plot of the age histogram using seaborn
sns.distplot(titanic['Age'], bins = 30, kde = False, color = 'red')


plt.show()


# #### Use the right plot to visualize column `Gender`. There are 2 ways of doing it. Do it both ways.
# **Hint**: Use matplotlib and seaborn.

# In[30]:


# Method 1 - matplotlib

# Bar plot of the gender
titanic['Gender'].value_counts().plot(kind='bar')

# Add labels to the plot and change xticks rotation
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation = 0)


plt.show()


# In[31]:


# Method 2 - seaborn

# Seaborn Countplot
sns.countplot(x ='Gender', data = titanic)

# Show the plot
plt.show()


# #### Use the right plot to visualize the column `Pclass`.

# In[32]:


# Bar plot of Pclass
titanic['Pclass'].value_counts().plot(kind='bar')

# Add labels to the plot and change xticks rotation
plt.xlabel('Class')
plt.ylabel('Count')
plt.xticks(rotation = 0)


plt.show()


# #### We would like to have in one single plot the summary statistics of the feature `Age`. What kind of plot would you use? Plot it. 

# In[33]:


# Box plot
titanic.boxplot(column='Age')

# Show the plot
plt.show()


# #### What does the last plot tell you about the feature `Age`?

# In[ ]:


"""
your comments here
"""
The statistics that you can get from the boxplot are the minimum, first quartile, median, 
third quartile, and maximum.

The red line shows us the median of Age. 
The blue box shows us the interquartile range (from Q1 to Q3).
It also shows us the outliers, which are out of the maximum and minimum range (Q1 - 1.5*IQR, Q3 + 1.5*IQR).


# #### Now in addition to the summary statistics, we want to have in the same plot the distribution of `Age`. What kind of plot would you use? Plot it. 

# In[34]:


# Set figure size
plt.figure(figsize = (15,8))

# Violin plot
sns.violinplot("Age", data = titanic)

# Show the plot
plt.show()


# #### What additional information does the last plot provide about feature `Age`?

# In[ ]:


"""
your comments here
"""
This plot is a combination of a boxplot and a density plot. The violin plot features a kernel density estimation 
of the underlying distribution of the data.

The black central part of the plot is the same as a boxplot and the white dot is the median.
The blue part is the distribution of the data.


# #### We suspect that there is a linear relationship between `Fare` and `Age`. Use the right plot to show the relationship between these 2 features. There are 2 ways, please do it both ways.
# **Hint**: Use matplotlib and seaborn.

# In[35]:


# Method 1 -

# Scatter plot
plt.scatter(titanic['Fare'], titanic['Age'])

# Add labels
plt.xlabel('Fare')
plt.ylabel('Age')

# Show the plot
plt.show()


# In[36]:


# Method 2 - seaborn


# Joinplot
sns.jointplot(x = 'Fare', y = 'Age', data = titanic)

# Show the plot
plt.show()


# #### Plot the correlation matrix using seaborn.

# In[40]:


# Set figure size
plt.figure(figsize = (10,8))

# Correlation matrix
sns.heatmap(titanic.corr(), cmap='coolwarm')

# Add title
plt.title('Correlation matrix')

# Show plot
plt.show()


# #### What are the most correlated features?

# In[ ]:


"""
your comments here
"""
The most correlated features are Parch and SibSp.


# #### Use the most appropriate plot to display the summary statistics of `Age` depending on `Pclass`.

# In[41]:


# Boxplot
sns.boxplot(x='Pclass',y='Age',data=titanic,palette='rainbow')

# Show the plot
plt.show()


# #### Use seaborn to plot the distribution of `Age` based on the `Gender`.
# **Hint**: Use Facetgrid.

# In[42]:


#method relplot
#sns.relplot(x='Gender', y='Age', hue="Gender", size="Age", data=data) 

# Create a grid with FacetGrid
g = sns.FacetGrid(data = titanic, col = 'Gender')

# Draw a plot on each facet
g.map(plt.hist, 'Age')

# Show the plot
plt.show()

