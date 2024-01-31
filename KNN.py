#!/usr/bin/env python
# coding: utf-8
# In[3]:
a=[]
b=[]
c=[]
import pandas as pd

x=int(input('enter the value of  x:'))
y=int(input('enter the value of y:'))
n= int(input("enter the value of n:"))
k= int(input("enter the value of k:"))

for i in range(n):
    ele =int(input())
    a.append(ele)
print(a)

for i in range(n):
    ele = int(input())
    b.append(ele)
print(b)

for i in range(n):
    summ = round(((a[i]-x)**2+(b[i]-y)**2)**0.5,3)
    c.append(summ)
print(c)

df = {"a":a,
     "b":b,
     "c":c}
df2 =pd.DataFrame(df)
df1=df2.sort_values(by='c')
df1['Rank']=range(1,len(df)+1)
print(df1)

k = k-1
res=df1.iloc[k-1,0:3]
res




