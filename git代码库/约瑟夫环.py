#!/usr/bin/env python
# coding: utf-8

# In[4]:


list1 = [i for i in range(1,40)] #自行更改范围
k = 0
while len(list1)>2 :
    i = 0
    while i<len(list1):
        k += 1
        if k == 3:    
            list1.remove(list1[i])
            k =0 
        else:
            i +=1
print(list1)

