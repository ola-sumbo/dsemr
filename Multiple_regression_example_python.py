#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


# ### Load the data

# In[2]:


data = pd.read_csv(r'C:\Users\LENOVO\Downloads\1.02. Multiple linear regression.csv')
data.head()


# In[3]:


data.describe()


# ### Create the multiple regression model

# In[4]:


y = data['GPA']
x1 = data[['SAT','Rand 1,2,3']] # x becomes a dataframe


# In[7]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# In[ ]:




