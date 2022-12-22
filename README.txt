# weather_forecast
Weather forecasting is the application of science and technology to predict the conditions of the atmosphere for a given location and time. People have attempted to predict the weather informally for millennia and formally since the 19th century. Weather forecasts are made by collecting quantitative data about the current state of the atmosphere, land, and ocean and using meteorology to project how the atmosphere will change at a given place. 
Dataset containing a Weather conditions Based on samples.
Weather forecasting now relies on computer-based models that take many atmospheric factors into account.[1] Human input is still required to pick the best possible forecast model to base the forecast upon, which involves pattern recognition skills, teleconnections, knowledge of model performance, and knowledge of model biases. The inaccuracy of forecasting is due to the chaotic nature of the atmosphere, the massive computational power required to solve the equations that describe the atmosphere, the land, and the ocean, the error involved in measuring the initial conditions, and an incomplete understanding of atmospheric and related processes. Hence, forecasts become less accurate as the difference between current time and the time for which the forecast is being made (the range of the forecast) increases. The use of ensembles and model consensus help narrow the error and provide confidence level in the forecast.
There is a vast variety of end uses to weather forecasts. Weather warnings are important forecasts because they are used to protect life and property. Forecasts based on temperature and precipitation are important to agriculture, and therefore to traders within commodity markets. Temperature forecasts are used by utility companies to estimate demand over coming days. On an everyday basis, many use weather forecasts to determine what to wear on a given day. Since outdoor activities are severely curtailed by heavy rain, snow and wind chill, forecasts can be used to plan activities around these events, and to plan ahead and survive them.
date
YYYY-MM-DD

precipitation
All forms in which water falls on the land surface and open water bodies as rain, sleet, snow, hail, or drizzle

temp_max
Maximum Temperature

temp_min
Minimum Temperature

wind
Wind speed

weather
output

Weather forecasting with Machine Learning, using Python
Simple, yet powerful application of Machine Learning for weather forecasting
The challenge I want to discuss is based on forecasting the average temperature using traditional machine learning algorithm:Decision Tree regressor.
So let’s start by describing the Python framework.

The libraries


import pandas as pd
import numpy as np
import matplotlib as plt 
import seaborn as sns 
import plotly.express as px 


The data set exploration.

#import the dataset.
p=r"C:\Users\chipp\Downloads\archive\seattle-weather.csv"
dt=pd.read_csv(p)

dt.head(10) ## gives first ten tuples from the dataset
dt.info() ## gives information about class,datatypes,row indices range,column attributes,memory usage;
dt.index ## gives the range from 0 to end;
dt["weather"].unique() ## gives array of unique weather conditions;
dt.nunique() ## gives the number of entries for each unique weather condition;
dt.value_counts ## gives the count of each and every day in dataset.
dt.weather.value_counts() ## gives the count of each weather condition in the whole data.
dt["date"]=pd.to_datetime(dt["date"]) ## convert date to datetime64;
dt["date"].dt.year ## This gives s,no,and year of each tuple.

the most frequent weather phenomena present
fig = px.histogram(dt, x="weather",text_auto=True ,color='weather',title='the most frequent weather phenomena presents').update_xaxes(categoryorder='total descending')
fig.show()

the most frequent weather phenomena presents(%
fig = px.pie(dt, names="weather",color='weather',title='the most frequent weather phenomena presents(%)')
fig.show()

sns.pairplot(dt,hue='weather')
plots the scatter plot for combinations of any two weather conditions.
 
 Boxplots
fig = px.box(dt, x="weather", y="precipitation")
fig.show()
fig = px.box(dt, x="weather", y="temp_max")
fig.show();
fig = px.box(dt, x="weather", y="wind")
fig.show()
fig = px.histogram(dt, x='weather',y="precipitation",color='weather',histfunc="avg",text_auto=True, title='Rainfall Averages').update_xaxes(categoryorder='total descending')
fig.show()
ig = px.histogram(dt, x='weather',y="temp_max",color='weather',histfunc="avg",text_auto=True, title='The highest average temperatures').update_xaxes(categoryorder='total descending')
fig.show()
fig = px.histogram(dt, x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest temperature averages').update_xaxes(categoryorder='total ascending')
fig.show()
fig = px.histogram(dt, x='weather',y="wind",color='weather',histfunc="avg",text_auto=True, title='Wind averages').update_xaxes(categoryorder='total ascending')
fig.show()
fig = px.histogram(dt[dt.date.dt.year==2012], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2012)').update_xaxes(categoryorder='total ascending')
fig.show()
fig = px.histogram(dt[dt.date.dt.year==2014], x='weather',y="temp_min",color='weather',histfunc="avg",text_auto=True, title='The lowest average temperatures (2014)').update_xaxes(categoryorder='total ascending')
fig.show()
sns.heatmap(dt.corr(),cmap = 'Wistia', annot= True)
dt.drop(columns={"date"},inplace=True)
x=dt.drop(columns={"weather"}).values
y=dt["weather"].values
y=pd.get_dummies(y)
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)
melbourne_model.score(x,y)*100
print("Votre Intelligence Arti est fiable à")
print(melbourne_model.score(x,y)*100),print("%")







