# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:08:02 2018

@author: Darko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "C:/Users/Darko/Downloads/tidytuesday-master/tidytuesday-master/data/week14_global_life_expectancy.csv"
data = pd.read_csv(filename)
print(data.columns)
data_gh = data[data.country == 'Ghana']
data_gh=data_gh.iloc[1:]
data_cd = data[data.country == "Cote d'Ivoire"]
data_to = data[data.country == 'Togo']
data_ben = data[data.country == 'Benin']
data_bf = data[data.country == 'Burkina Faso']

fig, ax1 = plt.subplots(figsize=(35, 7))
fig.subplots_adjust(left=0.115, right=0.88)
fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    
        
a=ax1.plot( 'year' , 'life_expectancy' , data=data_gh, marker = 'o', label ='ghana')
b=ax1.plot( 'year' , 'life_expectancy' , data=data_cd, marker = 'o', label ="Cote d'Ivoire")
c=ax1.plot( 'year' , 'life_expectancy' , data=data_to, marker = 'o', label ='togo')
d=ax1.plot( 'year' , 'life_expectancy' , data=data_ben, marker = 'o', label ='benin')
e = ax1.plot( 'year' , 'life_expectancy' , data=data_bf, marker = 'o', label ='burkina faso')
ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
ax1.yaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
    
ax1.set_xticks(list(data_gh.year))
ax1.set_xlabel('YEARS')
ax1.set_ylabel('LIFE EXPECTANCY')
ax1.legend(loc = 'best')
    
plt.title('life expectancy of Ghana and its neighbours')
plt.show()
fig.savefig('life_expectancy')



