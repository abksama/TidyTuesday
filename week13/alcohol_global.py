# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:02:06 2018

@author: Darko
"""

import pandas as pd
import matplotlib.pyplot as plt
filename ="C:/Users/Darko/Desktop/tidydata/tidytuesday-master/data/week13_alcohol_global.csv"
data = pd.read_csv(filename)
print(data.columns)
data_beer = data.sort_values('beer_servings', ascending = False)
data_beer = data_beer.head(15)
data_beer = data_beer.sort_values('beer_servings')

data_spirit = data.sort_values('spirit_servings', ascending = False)
data_spirit = data_spirit.head(15)
data_spirit = data_spirit.sort_values('spirit_servings')

data_wine = data.sort_values('wine_servings', ascending = False)
data_wine = data_wine.head(15)
data_wine = data_wine.sort_values('wine_servings')

data_total = data.sort_values('total_litres_of_pure_alcohol', ascending = False)
data_total = data_total.head(15) 
data_total = data_total.sort_values('total_litres_of_pure_alcohol')


fig = plt.figure(figsize = (15,15))
beer = fig. add_subplot(2, 2, 1)
spirit = fig. add_subplot(2, 2, 2)
wine = fig. add_subplot(2, 2, 3)
total = fig. add_subplot(2, 2, 4)

beer.barh(data_beer['country'], data_beer['beer_servings'])
beer.set_title('BEER SERVINGS (TOP 15)')
spirit.barh(data_spirit['country'], data_spirit['spirit_servings'])
spirit.set_title('SPIRIT SERVINGS (TOP 15)')
wine.barh(data_wine['country'], data_wine['wine_servings'])
wine.set_title('WINE SERVINGS (TOP 15)')
total.barh(data_total['country'], data_total['total_litres_of_pure_alcohol'])
total.set_title('TOTAL LITRES OF PURE ALCOHOL (TOP 15)')

fig.savefig('top 15 consumption')

