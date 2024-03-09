#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,classification_report


# In[5]:


actual = np.array(
	['Cat', 'Dog', 'Horse', 'Cat', 'Dog', 'Cat', 'Dog', 'Horse', 'Horse', 'Cat'])
predicted = np.array(
	['Cat', 'Dog', 'Dog', 'Cat', 'Dog', 'Cat', 'Dog', 'Horse', 'Horse', 'Dog'])


# In[6]:


cm = confusion_matrix(actual,predicted)


# In[20]:


sns.heatmap(cm,
           annot = True,
           fmt ='g',
           xticklabels=['Cat' ,'Dog','Horse'],
           yticklabels=['Cat'  , 'Dog',  'Horse'])
plt.title("confusion matrix" , fontsize = 18)
plt.xlabel('Actual',fontsize=15)
plt.ylabel('prediction',fontsize=15)
plt.show()

