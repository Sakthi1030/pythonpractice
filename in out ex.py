#!/usr/bin/env python
# coding: utf-8
# In[1]:
a=[]
for i in range(5):
    val = float(input("enter:"))
    a.append(val)
print(a)


# In[1]:
with open("sample-1.txt", "r") as fp:
    lines = fp.readlines()
with open("new_file.txt", "w") as fp:
    count = 0
    for line in lines: 
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1

