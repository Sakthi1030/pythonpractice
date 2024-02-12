#!/usr/bin/env python
# coding: utf-8

# In[16]:


a = []
b =[]
c =[]
n=5
for i in range(n):
   ab = int(input())
   a.append(ab)
print(a)
for i in range(n):
   ba = int(input())
   b.append(ba)
print(b)
x_bar = sum(a)/len(a)
y_bar = sum(b)/len(b)
for i in range(n):
   res = (a[i] - x_bar + b[i] - y_bar/ (a[i]- x_bar)**0.5)
   print( res)


