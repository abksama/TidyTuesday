# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 08:41:13 2018

@author: Darko
"""
import pandas as pd
from scipy import *
import matplotlib.pyplot as plt

filename1 = "C:/Users/Darko/Desktop/tidytuesday-master/data/2018-08-21/calfire_damage.csv"
filename = "C:/Users/Darko/Desktop/tidytuesday-master/data/2018-08-21/week21_calfire_frap.csv"
column = [ 'year_', 'agency', 'fire_cause', 'alarm_date']
data =pd.read_csv(filename, usecols = column)
data = data.dropna()
data['alarm_date'] = pd.to_datetime(data['alarm_date'])
data['month']= pd.DatetimeIndex(data['alarm_date']).month
data_mon = data.groupby(['year_','month','fire_cause'])[['alarm_date']].size().reset_index(name= 'tot_count')
col = []
for i in data_mon['fire_cause'].values:
    if(i == 'Natural'):
        col.append(1)
    elif(i == 'Human'):
         col.append(2)
    else:
         col.append(3)
         
data_mon['color']= col
print(data_mon)

data_human = data_mon[ data_mon['fire_cause']== 'Human']
data_nat= data_mon[ data_mon['fire_cause']== 'Natural']
data_un = data_mon[ data_mon['fire_cause']== 'Unknown']

x = []
y = []
area = []
color = []
for dat in data_mon:
    x.append(data_human['month'])
    y.append(data_human['year_'])
    area.append(data_human['tot_count']*20)
    
    
x1 = []
y1 = []
area1 = []
for dat in data_mon:
    x1.append(data_nat['month'])
    y1.append(data_nat['year_'])
    area1.append(data_nat['tot_count']*20)
    
x2 = []
y2 = []
area2 = []
for dat in data_mon:
    x2.append(data_un['month'])
    y2.append(data_un['year_'])
    area2.append(data_un['tot_count']*20)    
    
fig, ax1 = plt.subplots(figsize=(9, 25))
fig.subplots_adjust(left=0.115, right=0.88)
fig.canvas.set_window_title('Eldorado K-8 Fitness Chart')
plt.minorticks_on()
ax1.yaxis.grid(True, linestyle='--', which='both',
                   color='green', alpha=.65)
plt.minorticks_on()
    
sct = ax1.scatter(x,y,  s = area)
sc =ax1.scatter(x1,y1,  s = area1)
si =ax1.scatter(x2,y2,  s = area2)
ax1.legend((sct,sc,si),('Natural','Human','Unknown'))
ax1.set_xlabel('MONTHS')
ax1.set_ylabel('YEAR')
plt.title('FIRE OUTBREAKS IN CALIFORNIA')

plt.show()
fig.savefig('fire outbreaks')
