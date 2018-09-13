# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:10:14 2018

@author: Darko
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap as Basemap 
#from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from pandas import Series, DataFrame
filename = "C:/Users/Darko/Downloads/tidytuesday-master/tidytuesday-master/data/week15_beers.xlsx"
data = pd.read_excel(filename, na_values=['NA'], sheetname = 'breweries')
data_brew = data.groupby('state')[['name']].size().reset_index(name = 'number_of_breweries') 
print(data_brew)
#ab = data_brew.set_index('state').T.to_dict('list')
#print(ab)
