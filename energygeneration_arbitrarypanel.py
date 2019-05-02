# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:02:51 2019

@author: Nicole
"""

import pandas as pd
import matplotlib.pyplot as plt

'''Energy Generation for Panasonic Panel'''

'''Fixed Parameters'''

areacovered = 12000 # m^2

'''Variable Inputs'''

efficiencyPV = 0.15

'''Importing Irradiance Data and Calculating Energy Generation'''

df1 = pd.read_csv('PVGIS_39deg_-5deg_2015_2016.csv', usecols=[9])
energygeneration = efficiencyPV*areacovered*df1.values/1000 #kWh

'''Plotting the Energy Generation Profile'''

plt.plot(energygeneration)
plt.title('Energy Generation Over One Year')
plt.ylabel('Energy Generation (kWh)')
plt.xlabel('Month')
plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.savefig('Report/Pics_NK/energygeneration_39deg_arbitrarypanel.jpg',dpi = 1000)