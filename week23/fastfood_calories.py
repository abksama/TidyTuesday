# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:52:29 2018

@author: Darko
"""

import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

filename = "C:/Users/Darko/Desktop/tidytuesday-master/data/2018-09-04/fastfood_calories.csv"
data =pd.read_csv(filename)
data = data.dropna()
print(data.columns)
data_cal = data.groupby('restaurant', observed = True)[['calories']].mean().reset_index()
data_max = data.groupby('restaurant', observed = True)[['item','calories']].max().reset_index()
data_min = data.groupby('restaurant', observed = True)[['item','calories']].min().reset_index()
data_cho = data.groupby('restaurant', observed = True)[['cholesterol']].mean().reset_index()
data_max_cho = data.groupby('restaurant', observed = True)[['item','cholesterol']].max().reset_index()
print(data_cal)
print(data_max)
print(data_min)
print(data_cho)
print(data_max_cho)


res = list(data_cal.restaurant)
    
def pro(dat, lab, save):
    
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    pos = np.arange(len(res))
    
    rects = ax1.barh(pos, dat,
                         align='center',
                         height=0.5, color='m',
                         tick_label=res, edgecolor = ".2")
    ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='grey', alpha=.25)
    
    rect_labels = []
    for rect in rects:
        
        width = int(rect.get_width())

        rankStr = list(lab[dat==rect.get_width()])
        # The bars aren't wide enough to print the ranking inside
        if (width < 250 ):
            xloc = width + 1
            clr = 'black'
            align = 'left'
        else:
            
            xloc = 0.98*width
            clr = 'white'
            align = 'right'

        yloc = rect.get_y() + rect.get_height()/2.0
        label = ax1.text(xloc, yloc, rankStr, horizontalalignment=align,
                         verticalalignment='center', color=clr, weight='bold',
                         clip_on=True)
        rect_labels.append(label)
    
    plt.show()
    fig.savefig(save)
    
pro(data_cal.calories,data_cal.restaurant, 'avg_calories')     
pro(data_min.calories, data_min.item, 'min_calories') 
pro(data_max.calories, data_min.item, 'max_cal')  
pro(data_cho.cholesterol,data_cho.restaurant, 'avg_chol') 



 
