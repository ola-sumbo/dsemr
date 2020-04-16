#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# In[2]:


data = pd.read_csv(r'C:\Users\LENOVO\Downloads\1.01. Simple linear regression.csv')
data


# In[3]:


data.describe()


# ### Define your independent and dependent variable 

# In[4]:


y = data['GPA']
x1 = data['SAT']


# In[5]:


## Explore the data through plotting


# In[7]:


plt.scatter(x1, y)
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize =20)
plt.show() #each point represent a student on the graph


# #### Regression itself

# In[9]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# ### Plotting the fitted regression line

# In[10]:


# line closest to all observation is the line of best fit 


# In[12]:


plt.scatter(x1, y)
y_hat = 0.0017* x1 + 0.275
fig = plt.plot(x1, y_hat, lw=4, c='purple',label='fitted regression line')
plt.xlabel('SAT',fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()


# In[ ]:




