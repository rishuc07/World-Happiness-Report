#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Use the World Happiness Report, which is a survey about the state of global happiness. The report ranks more than 150 countries by their happiness levels, and has been published almost every year since 2012. We'll use data collected in the years 2015, 2016, and 2017

#• Which are the happiest and least happy countries and regions in the world?

#• Is happiness affected by region?

#• Did the happiness score change significantly over the past three years?


# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df_happiness = pd.read_csv('C:\\Users\\SN Shashank\\Downloads\\Rishabh\\World_Happiness_data\\worldhappiness.csv')


# In[4]:


df_happiness.head()


# In[15]:


df_happiness.loc[df_happiness['Happiness Rank'] == 1]   


# In[16]:


df_happiness.columns


# In[17]:


df_happiness.index


# In[26]:


#Is happiness affected by region?
hp_affected=df_happiness.groupby('Region')['Happiness Score'].sum()
hp_affected


# In[29]:


hp_affected.plot.pie(autopct = '%1.1f%%')
plt.title('Happiness Score')


# In[36]:


#Did the happiness score change significantly over the past three years?
df_happiness.loc[df_happiness['Country'] == 'Denmark' ]  


# In[ ]:




