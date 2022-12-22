#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt 
import seaborn as sns 
import plotly.express as px 

#importons le dataset 
p=r"C:\Users\chipp\Downloads\archive\seattle-weather.csv"
dt=pd.read_csv(p)


# # Studies of the dataset

# In[2]:


dt.head(10)


# In[3]:


dt.info()


# In[4]:


dt.index


# In[5]:


dt["weather"].unique()


# In[6]:


dt.nunique()


# In[7]:


dt.count()


# In[8]:


dt.value_counts


# In[9]:


dt.weather.value_counts()


# # convert date to datetime64

# In[10]:


dt["date"]=pd.to_datetime(dt["date"])


# In[11]:


dt.info()


# # Visualisation
# 

# In[12]:


dt["date"].dt.year


# In[13]:


fig = px.histogram(dt, x="weather",text_auto=True ,color='weather',title='the most frequent weather phenomena presents').update_xaxes(categoryorder='total descending')
fig.show()


# In[14]:


fig = px.pie(dt, names="weather",color='weather',title='the most frequent weather phenomena presents(%)')
fig.show()


# In[17]:


sns.pairplot(dt,hue='weather')


# In[16]:


fig = px.box(dt, x="weather", y="precipitation")
fig.show()


# ## only "Rain" and "snow" have precipitation, Rain has outliers##

# In[18]:


fig = px.box(dt, x="weather", y="temp_max")
fig.show()


# # Sun" has the highest temperatures , "Rain" has outliers

# In[19]:


fig = px.box(dt, x="weather", y="temp_min")
fig.show()


# # "snow" has the lowest temperatures , "Sun" and "Snow" have outliers

# In[20]:


fig = px.box(dt, x="weather", y="wind")
fig.show()


# # "Snow" has the strongest values , Only snow does not have outliers

# In[22]:


fig = px.histogram(dt, x='weather',y="precipitation",color='weather',histfunc="avg",text_auto=True, title='Rainfall Averages').update_xaxes(categoryorder='total descending')
fig.show()


# In[23]:


fig = px.histogram(dt, x='weather',y="temp_max",color='weather',histfunc="avg",text_auto=True, title='The highest average temperatures').update_xaxes(categoryorder='total descending')
fig.show()


# In[24]:


fig = px.histogram(dt, x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest temperature averages').update_xaxes(categoryorder='total ascending')
fig.show()


# In[25]:


fig = px.histogram(dt, x='weather',y="wind",color='weather',histfunc="avg",text_auto=True, title='Wind averages').update_xaxes(categoryorder='total ascending')
fig.show()


# In[26]:


fig = px.histogram(dt[dt.date.dt.year==2012], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2012)').update_xaxes(categoryorder='total ascending')
fig.show()


# In[32]:


fig = px.histogram(dt[dt.date.dt.year==2013], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2013)').update_xaxes(categoryorder='total ascending')
fig.show()


# In[30]:


fig = px.histogram(dt[dt.date.dt.year==2014], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2014)').update_xaxes(categoryorder='total ascending')
fig.show()


# In[33]:


fig = px.histogram(dt[dt.date.dt.year==2015], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2015)').update_xaxes(categoryorder='total ascending')
fig.show()


# In[34]:


sns.heatmap(dt.corr(),cmap = 'Wistia', annot= True)


# In[35]:


dt.drop(columns={"date"},inplace=True)
x=dt.drop(columns={"weather"}).values
y=dt["weather"].values


# In[36]:


y=pd.get_dummies(y)


# In[37]:


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)
melbourne_model.score(x,y)*100
print("Your Arti Intelligence is reliable at")
print(melbourne_model.score(x,y)*100),print("%")


# In[ ]:




