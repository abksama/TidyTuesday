# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 15:03:06 2018

@author: Darko
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
filename = "C:/Users/Darko/Downloads/tidytuesday-master/tidytuesday-master/data/week18_dallas_animals.xlsx"
data = pd.read_excel(filename,  sheet_name='simple', na_values=['NA'])
animal_type = data.groupby('animal_type')[['animal_type']].size().reset_index(name = 'count')
data['intake_date'] = pd.to_datetime(data['intake_date'])
data['month1']= pd.DatetimeIndex(data['intake_date']).month
animals_mon = data.groupby(['year', 'month1', 'month'], observed = True)[['animal_type']].size().reset_index(name = 'count')



def plott(data, name):
    fig, ax2 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    
        
    ax2.plot( 'month' , 'count' , data=data, marker = 'o')
    ax2.xaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
    ax2.yaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
    
    ax2.set_xticks(list(animals_mon.month))
    ax2.set_xlabel('MONTH')
    ax2.set_ylabel('NUMBER OF ANIMALS')
    
    plt.title(name)
    plt.show()
    fig.savefig('line graph')
plott(animals_mon, "count of animals by month from  2016 - 2017")

fig, ax1 = plt.subplots(figsize=(9, 7))
fig.subplots_adjust(left=0.115, right=0.88)
fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    
ax1.pie(animal_type['count'],labels = animal_type['animal_type'], shadow = True, autopct = '%1.2f%%' )
plt.axis('equal')
plt.show()
fig.savefig('pie chart')

