#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Anagrams
a = str(input("enter:"))
b = str(input("enter:"))
if sorted(a)==sorted(b):
    print("True")
else:
    print("False")


# In[10]:


#WORD COUNT
def word_count(a):
    words = a.split()
    word ={}
    for i in words:
        i = i.lower().strip("?!,.")
        if i.isalpha:
            if i in word:
                word[i] += 1
            else:
                word[i] = 1
    return word
a = "Hello , welcome guys! and Hello to the world of python."
print(word_count(a))


# In[8]:


#check for prime number 
div = range(2,10)
num = int(input("enter :"))
if num == 2:
    print("prime")


for i in range(2,10):
        if num%i == 0:
            print("not prime")
            
    
else :
    print("it is prime")


# In[6]:


#finding common elemnts between lists
l1=[]
l2=[]
n = int(input("enter the value of n :"))
for i in range (n):
    a = input("l1 value:")
    b = input("l2 value:")
    l1.append(a)
    l2.append(b)
print(l1)
print(l2)
res= set(l1)&set(l2)
print(res)


# In[ ]:




