#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Today, we're learning about a new data type: sets.
m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
symeteric_difference = a.difference(b).union(b.difference(a))
for i in sorted(symeteric_difference):
    print(i)


# In[ ]:




