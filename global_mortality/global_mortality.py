# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:57:01 2018

@author: Darko
"""


import pandas as pd
import matplotlib.pyplot as plt

filename = 'C:/users/Darko/desktop/tidydata/global_mortality.xlsx'
data = pd.read_excel(filename, na_values= None)
data = data[(data['country'])== 'Ghana']
data = data.dropna()

data_2016 = data[data['year']==2016]
data_2015 = data[data['year']==2015]
data_2014 = data[data['year']==2014]

years = list(data['year'])

 
data_2016 = data_2016.drop(['country','country_code','year'], axis=1)
b = data_2016.loc[2105]
b = b.sort_values(ascending = True)

data_2015 = data_2015.drop(['country','country_code','year'], axis=1)
c = data_2015.loc[2104]
c = c.sort_values(ascending = True)

data_2014 = data_2014.drop(['country','country_code','year'], axis=1)
a = data_2014.loc[2103]
a = a.sort_values(ascending = True)
plt. figure(figsize = (20,20))
plt.title('2016 cause of death for Ghana')
b.plot.barh()
plt.savefig('2016 cause of death') 

plt. figure(figsize = (20,20))
plt.title('2015 cause of death for Ghana')
c.plot.barh()
plt.savefig('2015 cause of death') 

plt. figure(figsize = (20,20))
plt.title('2014 cause of death for Ghana')
a.plot.barh()
plt.savefig('2014 cause of death') 




data = data.drop(['country','country_code','year'], axis=1)
data = data.T

data.columns = years

data = data.sort_values(2016, ascending = False)
print(data)
data = data.truncate(after = 'HIV/AIDS (%)')
data = data.T
print(data)

plt.figure(figsize = (20,20))
data.plot()
plt.title('Top 6 Cause of Death Line Plot for Ghana')
plt.minorticks_on()
plt.xlabel('YEARS')
plt.savefig('top 6 cause of death') 


