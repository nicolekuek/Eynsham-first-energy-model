# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:02:51 2019

@author: Nicole
"""

import pandas as pd
import matplotlib.pyplot as plt

'Fixed Parameters'

areaPV_panasonic = 1.59004 * 1.0541 # m^2

'Variable Inputs'

efficiencyPV_panasonic = 0.197
numberPVs_panasonic = 7159

'Importing Irradiance Data and Calculating Energy Generation'

areacovered_panasonic = areaPV_panasonic*numberPVs_panasonic #m^2 (area of parking spaces covered, 12000m^2 maximum)

'Using averaged data from 2015 to 2016 at 39 degree slope'
#df1 = pd.read_csv('PVGIS_39deg_-5deg_2015_2016.csv', usecols=[9])

'Using only 2016 data at 21.8 degree slope'
#df1 = pd.read_csv('PVGIS_21.8deg_-5deg_2016.csv', usecols=[9])

'Using averaged data from 2007 to 2016 at 21.8 degree slope'
df1 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[9])

'Use this to find generation for first 2 sets of data'
#energygen_panasonic = efficiencyPV_panasonic*areacovered_panasonic*df1.values/1000 #kWh (use for first 2 csv files)

'Use this to find generation using data averaged between 2007 and 2016'
energygen_panasonic = efficiencyPV_panasonic*areacovered_panasonic*df1.values #kWh (W to kW conversion already done in Excel)

'Plotting the energy generation profiles'

plt.plot(energygen_panasonic)
plt.title('Energy Generation Over One Year')
plt.ylabel('Panasonic Energy Generation (kWh)')
plt.xlabel('Month')
plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.savefig('Report/Pics_NK/avgenergygeneration_22deg_panasonicpanel.jpg',dpi = 1000)

#%%

'''Monthly generation'''

'Total generation in January'
jan = energygen_panasonic[:744]
total_jan = float(sum(jan))

'Total generation in February'
feb = energygen_panasonic[744:1416]
total_feb = float(sum(feb))

'Total generation in March'
mar = energygen_panasonic[1416:2160]
total_mar = float(sum(mar))

'Total generation in April'
apr = energygen_panasonic[2160:2880]
total_apr = float(sum(apr))

'Total generation in May'
may = energygen_panasonic[2880:3624]
total_may = float(sum(may))

'Total generation in June'
jun = energygen_panasonic[3624:4344]
total_jun = float(sum(jun))

'Total generation in July'
jul = energygen_panasonic[4344:5088]
total_jul = float(sum(jul))

'Total generation in August'
aug = energygen_panasonic[5088:5832]
total_aug = float(sum(aug))

'Total generation in September'
sep = energygen_panasonic[5832:6552]
total_sep = float(sum(sep))

'Total generation in October'
oct = energygen_panasonic[6552:7296]
total_oct = float(sum(oct))

'Total generation in November'
nov = energygen_panasonic[7296:8016]
total_nov = float(sum(nov))

'Total generation in December'
dec = energygen_panasonic[8016:8760]
total_dec = float(sum(dec))

'Plot monthly generation'

plt.figure()
monthlygeneration = [total_jan,total_feb,total_mar,total_apr,total_may,total_jun,total_jul,total_aug,total_sep,total_oct,total_nov,total_dec]
plt.plot(monthlygeneration)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.title('Monthly Energy Generation Over One Year')
plt.xlabel('Month')
plt.ylabel('Panasonic Energy Generation (kWh)')
plt.ylim(ymin=0)
plt.savefig('Report/Pics_NK/avgenergygeneration_22deg_panasonicpanel_monthly.jpg', dpi = 1000, bbox_inches = "tight")

#%% Average hourly generation for each month of the year

'Used in total_x_kWh txt files'

print('Average hourly generation on a day in January')
jan = energygen_panasonic[:744] # 24*31 = 744 (no. values of solar_profile that correspond to Jan)
for i in range(24):
    print(float(sum(jan[i::24])/31))

print('Average hourly generation on a day in February')
feb = energygen_panasonic[744:1416]
for i in range(24):
    print(float(sum(feb[i::24])/28))
    
print('Average hourly generation on a day in March')
mar = energygen_panasonic[1416:2160]
for i in range(24):
    print(float(sum(mar[i::24])/31))

print('Average hourly generation on a day in April')
apr = energygen_panasonic[2160:2880]
for i in range(24):
    print(float(sum(apr[i::24])/30))
    
print('Average hourly generation on a day in May')
may = energygen_panasonic[2880:3624]
for i in range(24):
    print(float(sum(may[i::24])/31))
    
print('Average hourly generation on a day in June')
jun = energygen_panasonic[3624:4344]
for i in range(24):
    print(float(sum(jun[i::24])/30))
    
print('Average hourly generation on a day in July')
jul = energygen_panasonic[4344:5088]
for i in range(24):
    print(float(sum(jul[i::24])/31))
    
print('Average hourly generation on a day in August')
aug = energygen_panasonic[5088:5832]
for i in range(24):
    print(float(sum(aug[i::24])/31))
    
print('Average hourly generation on a day in September')
sep = energygen_panasonic[5832:6552]
for i in range(24):
    print(float(sum(sep[i::24])/30))
    
print('Average hourly generation on a day in October')
oct = energygen_panasonic[6552:7296]
for i in range(24):
    print(float(sum(oct[i::24])/31))
    
print('Average hourly generation on a day in November')
nov = energygen_panasonic[7296:8016]
for i in range(24):
    print(float(sum(nov[i::24])/30))
    
print('Average hourly generation on a day in December')
dec = energygen_panasonic[8016:8760]
for i in range(24):
    print(float(sum(dec[i::24])/31))