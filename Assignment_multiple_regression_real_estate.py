#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


# ### load the dataset

# In[5]:


data = pd.read_csv(r'C:\Users\LENOVO\Downloads\real_estate_price_size_year.csv')
data.head()


# In[6]:


data.describe()


# ### create multiple regression model for housing prices 

# In[7]:


y = data['price']
x1 = data[['size', 'year']] 


# In[9]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# In[ ]:




