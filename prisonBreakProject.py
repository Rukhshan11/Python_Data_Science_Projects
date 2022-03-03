#!/usr/bin/env python
# coding: utf-8

# In[1]:


welcome_message = 'Hello, Jupyter. '


# In[2]:


result = 1200 / 12


# In[3]:


print(welcome_message)
print(result)


# In[4]:


print('New Cell')


# In[5]:


print('Another new cell')


# In[10]:


# My First Data Science Project
# We begin by importing some helper functions.
from helper import *


# In[11]:


# Helicopter Escapes!
url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# In[12]:


for row in data[ :3]:
    print(row)


# In[12]:


index = 0
for row in data:
    data[index] = row[ :-1]
    index += 1
print(data[ :3])


# In[13]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[14]:


print(data[:3])


# In[15]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]
print(min_year)
print(max_year)


# In[16]:


years = []
for y in range(min_year, max_year + 1):
    years.append(y)
print(years)


# In[19]:


attempts_per_year=  []
for y in years:
    attempts_per_year.append([y, 0])
    


# In[21]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
print(attempts_per_year)
            


# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[28]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:




