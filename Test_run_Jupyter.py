#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


scalar = 5
vector = np.array([5,-2,4])
matrices = np.array([[5,12,6],[-3,0,14]])


# In[3]:


scalar


# In[4]:


vector


# In[5]:


matrices


# # This is with regards to datatypes

# In[8]:


type(scalar)


# In[9]:


type(vector)


# In[10]:


type(matrices)


# In[11]:


## convert scalars to arrays


# In[12]:


s_arrays = np.array(scalar)


# In[13]:


s_arrays


# In[14]:


type(s_arrays)


# ### This is the segment for data shapes 

# In[15]:


matrices.shape


# In[16]:


vector.shape


# In[17]:


vector.reshape


# In[18]:


scalar.shape


# In[19]:


s_arrays.shape


# In[20]:


vector.reshape


# In[ ]:




