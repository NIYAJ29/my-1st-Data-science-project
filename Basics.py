#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data

# ## Prison Helicopter Escapes

# In[69]:


from helper import *


# ## Get the Data

#  Now, let's get the data from the 'List of helicopter prison escapes' (https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# Let's print the first three rows

# In[53]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)

for i in data[:3]:
    print(i)


# ## removing Details

# In[54]:


index = 0
for i in data:
    data[index] = i[:-1]
    index += 1
    
print(data[:3])


# ## changing date format

# In[55]:


for i in data:
    i[0] = fetch_year(i[0])


# In[56]:


print(data[:3])


# ## attempts per year

# In[57]:


min_year = min(data, key = lambda x : x[0])[0]
max_year = max(data, key = lambda x : x[0])[0]


# In[58]:


print(min_year)
print(max_year)


# now make a list of years including min and max

# In[59]:


years = []
for i in range(min_year, max_year + 1):
    years.append(i)


# In[60]:


print(years)


# ## making a list attemps per year

# In[64]:


attempts_per_years = []

for year in years:
    attempts_per_years.append([year,0])
    
    
print(attempts_per_years)
        


# In[65]:


for i in data :
    for year_attempt in attempts_per_years:
        year = year_attempt[0]
        if i[0] == year:
            year_attempt[1] += 1
            
print(attempts_per_years)


# In[67]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_years)


# In[75]:


countries_frequency = df["Country"].value_counts()
print_pretty_table(countries_frequency)


# In[ ]:




