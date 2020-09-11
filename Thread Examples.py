#!/usr/bin/env python
# coding: utf-8

# In[24]:


import threading


# In[25]:


print("Example-1")


# In[26]:


def loop1():
    for i in range(1,20000):
        print("1", end="")
        
def loop2():
    for i in range(1,5000):
        print("2", end="")


# In[27]:


loop1()
loop2()


# In[31]:


thread1 = threading.Thread(target = loop1)
thread2 = threading.Thread(target = loop2)

thread1.start()
thread2.start()


# In[30]:


print("Example-2")


# In[46]:


import time


# In[78]:


## TEST
## time1=1,time2=4, time3=2 -> output: AAA 6 BBB DDD CCC
## time1=1, time2=1, time3=1 -> output: AAA 6 DDDBBB CCC
## time1=1, time2=1, time3=3 -> output: AAA6 BBB CCC DDD
def func():
    print("AAA")
    time.sleep(4) # time1
    print("BBB")
    time.sleep(1) # time2
    print("CCC")


# In[80]:


t1 = threading.Thread(target= func)
t1.start()
print(threading.activeCount())
time.sleep(2) # time3
print("DDD")


# In[ ]:




