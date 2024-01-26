#!/usr/bin/env python
# coding: utf-8

# 
# 
# ## string methods
# 

# In[5]:


a = 'sakthi'
b = "SAKTHI VEL RAVICHANDRAN"
print(a.capitalize())
print(a.count(a))
print(b.center(110))
print(b.casefold())
print(b.encode())
print(a.encode())
print(b.expandtabs(10))


# ### boolean methods

# In[8]:


a = 75
b = 45
if a<= b:
    print('ryt')
else:
    print('okok')


# In[17]:


none = 0
bool(none)
print(bool(0))
print(bool(""))


# In[3]:


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# In[10]:


# python program to check the common letters in string 
def common():
    s1 = input('enter:')
    s2 = input('enter:')
    lis1 = set(s1)
    lis2 = set(s2)
    com = lis1 & lis2
    
    print(com)
common()


# In[ ]:




