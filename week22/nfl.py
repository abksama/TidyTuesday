# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 15:15:08 2018

@author: Darko
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "C:/Users/Darko/Desktop/tidytuesday-master/data/2018-08-28/nfl_2010-2017.csv"
column = ['name','team','game_year','game_week', 'rush_att','rush_yds', 'rush_avg','rush_tds','rush_fumbles', 'position']
data =pd.read_csv(filename, usecols = column)
data = data.dropna()

data_sot = data.groupby(['position','game_year'], observed = True )[['rush_yds','rush_att']].mean().reset_index()
data_qb = data_sot[data_sot['position']=='QB']
data_rb = data_sot[data_sot['position']=='RB']
data_wr = data_sot[data_sot['position']=='WR/TE']
print(data_qb)
def plott(data, name, save):
    fig, ax1 = plt.subplots(figsize=(9, 7))
    fig.subplots_adjust(left=0.115, right=0.88)
    fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
    
        
    ax1.plot( 'game_year' , 'rush_yds' , data=data, marker = 'o')
    ax1.xaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
    ax1.yaxis.grid(True, linestyle='--', which='major',
                   color='green', alpha=.65)
    
    ax1.set_xticks(list(data_qb.game_year))
    ax1.set_xlabel('YEARS')
    ax1.set_ylabel('RUSH YARDS')
    
    plt.title(name)
    plt.show()
    fig.savefig(save)
    
plott(data_qb, 'QB RUSH YARDS', 'qb')
plott(data_rb, 'RB RUSH YARDS', 'rb')
plott(data_wr, 'WR/TE RUSH YARDS', 'wr_te')

# =============================================================================
# plt.plot('game_year' , 'rush_yds' , data=data_rb)
# =============================================================================

