#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# In[27]:


data = pd.read_csv(r'C:\Users\LENOVO\Downloads\real_estate_price_size.csv')
data.head()


# In[3]:


data.describe()


# ## Define the dependent and independent variable

# In[33]:


y = data['price']
x1 = data['size']


# In[29]:


# Explore the data through plotting


# In[34]:


plt.scatter(x1, y)
plt.xlabel('size', fontsize = 20)
plt.ylabel('price', fontsize =20)
plt.show()  #each point represents houses 


# In[31]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# ## Plotting the fitted regression line

# In[11]:


# line that captures most of the observation is the line of best fit


# In[32]:


plt.scatter(x1, y)
y_hat = x1*223.1787+101900
fig = plt.plot(x1, y_hat, lw=4, c ='red', label='fitted regression line')
plt.xlabel('Size', fontsize = 20)
plt.ylabel('Price', fontsize = 20)
plt.show()


# In[ ]:




