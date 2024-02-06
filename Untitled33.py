#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd



# In[4]:


dates = pd.date_range(start='2021-01-01', end='2021-12-31', periods=500)


# In[12]:


import numpy as np
likes = np.random.randint(0, 10000, size=500)
dates = pd.date_range(start='2021-01-01', end='2021-12-31', periods=500)


# In[13]:


data = dict(zip(['Date', 'Category', 'Likes'], [dates, category, likes]))


# In[1]:


df = pd.DataFrame(data)


# In[ ]:




