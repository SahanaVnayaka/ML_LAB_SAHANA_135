#!/usr/bin/env python
# coding: utf-8

# In[6]:


#mean
def mean(list):
    
    sum=0
    for i in list:
        sum=sum+i
        
    mean=sum/len(list)
    return mean
list=(5,10,15,20,25,30)
print("MEAN:",mean(list))


# In[7]:


#median

s=(5,10,15,20,25,30)
x=int(len(s)/2)
if x%2==0:
    result=(s[x]+s[x+1]/2)
else:
    result=s[x]
print("MEDIAN:",result)    


# In[8]:


#mode
s=(5,10,10,15,20,25,30)
d={}
for x in s:
    if x in d:
        d[x]=d[x]+1
    else:
        d[x]=1
maxx=0
for x in d:
    if(d[x]>maxx):
        maxx=d[x]
        answer=x
print("MODE:",answer)        


# In[9]:


#variance
def variance(x):
    answer=mean(x)
    
    sum=0
    for s in x:
        sum+=(answer-s)**2
        
    return sum/len(x)
x=(5,10,15,20,25,30)
print("VARIANCE:",variance(x))


# In[10]:


#standard deviation
def standevi(x):
    temp=variance(x)
    return temp**0.5
x=(5,10,15,20,25,30)
print("STANDARD DEVIATION:",standevi(x))


# In[ ]:




