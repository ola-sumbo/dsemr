#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


# In[7]:


raw_data = pd.read_csv(r'C:\Users\LENOVO\Downloads\1.03. Dummies.csv')
raw_data.head()


# In[8]:


data = raw_data.copy()
data['Attendance'] = data['Attendance'].map({'Yes':1, 'No': 0})
data.head(10)


# In[9]:


data.describe() #more than 75% is 0.46 as mean is lower than 0.5 we have more nos than yes


# ## Regression

# In[10]:


y = data['GPA']
x1 = data[['SAT','Attendance']]


# In[11]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()


# ## Plotting data for y_hat categorical

# In[13]:


plt.scatter(data['SAT'], y)
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665+0.0014*data['SAT']
fig = plt.plot(data['SAT'],yhat_no, lw=2, color ='#006837')
fig = plt.plot(data['SAT'],yhat_yes, lw=2, color ='#a50026')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize=20)
plt.show()  # same slope but different intercept


# ### Color points that have 75% which is 46% of yes

# In[22]:


plt.scatter(data['SAT'],data['GPA'],c = data['Attendance'],cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665+0.0014*data['SAT']
fig = plt.plot(data['SAT'],yhat_no, lw=2, color ='#006837')
fig = plt.plot(data['SAT'],yhat_yes, lw=2, color ='#a50026')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize=20)
plt.show()


# ### Addition of the original regression line

# In[25]:


plt.scatter(data['SAT'],data['GPA'],c = data['Attendance'],cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']
yhat_yes = 0.8665 + 0.0014*data['SAT']
yhat = 0.0017*data['SAT'] + 0.275
fig = plt.plot(data['SAT'],yhat_no, lw=2, color ='#006837',label='regression line 1')
fig = plt.plot(data['SAT'],yhat_yes, lw=2, color ='#a50026',label='regression line 2')
fig = plt.plot(data['SAT'],yhat,lw=3, color ='#4C72B0', label ='fitted regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize=20)
plt.show()


# In[ ]:




