# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:02:51 2019

@author: Nicole
"""

import pandas as pd
import matplotlib.pyplot as plt

'''Comparing Panasonic and JXSOL Panel Outputs'''

'Fixed Parameters'

areaPV_panasonic = 1.59004 * 1.0541 # m^2
areaPV_JXSOL = 1.956*0.992 # m^2

'Variable Inputs'

efficiencyPV_panasonic = 0.197
efficiencyPV_JXSOL = 0.18

numberPVs_panasonic = 7159
numberPVs_JXSOL = 6184

'Importing Irradiance Data and Calculating Energy Generation'

areacovered_panasonic = areaPV_panasonic*numberPVs_panasonic #m^2
areacovered_JXSOL = areaPV_JXSOL*numberPVs_JXSOL # m^2

'Using averaged data from 2010 to 2016 at 21.8 degree slope'
df1 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[9])

energygen_panasonic = efficiencyPV_panasonic*areacovered_panasonic*df1.values #kWh
energygen_JXSOL = efficiencyPV_JXSOL*areacovered_JXSOL*df1.values

'Plotting the energy generation profiles'

plt.plot(energygen_panasonic, label = 'Panasonic')
plt.plot(energygen_JXSOL, label = 'JXSOL')
plt.title('Energy Generation Over One Year')
plt.ylabel('Panasonic Energy Generation (kWh)')
plt.xlabel('Month')
plt.legend(title = 'Solar Panel Model')
plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#plt.savefig('Report/Pics_NK/energygeneration_comparison.jpg',dpi = 1000)

'Plotting the difference between energy generation profiles'

plt.figure()
difference = energygen_JXSOL - energygen_panasonic
plt.plot(difference)
plt.title('Difference in Energy Generation')
plt.ylabel('Energy Generation (kWh)')
plt.xlabel('Month')
plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#plt.savefig('Report/Pics_NK/energygeneration_JXSOLpanel.jpg',dpi = 1000)
