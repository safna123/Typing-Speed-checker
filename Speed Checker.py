#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time as t


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


Typing_word = "Type the word 'supercalifragilisticexpialidocious' for 5 times to test your accuracy and time taken."


# In[4]:


input_list = []


# In[5]:


time_list = []


# In[6]:


print(Typing_word)


# In[7]:


mistakes = 0


# In[8]:


for x in range(0,5):
    start = t.time()
    user_input = input("Print the word again ")
    end = t.time()
    time_elapsed = end - start
    input_list.append(user_input)
    time_list.append(time_elapsed)
    if(user_input.lower() != 'supercalifragilisticexpialidocious'):
        mistakes += 1


# In[9]:


print(input_list)


# In[10]:


print(time_list)


# In[34]:


print("Mistakes done on Typing check is ",mistakes)


# In[12]:


x = [1,2,3,4,5]


# In[37]:


markerline, stemlines, baseline = plt.stem(
    x, time_list, linefmt='gray', markerfmt='D', bottom=0.2)
markerline.set_markerfacecolor('blue')
plt.ylabel("Time_taken")
plt.show()


# In[14]:




