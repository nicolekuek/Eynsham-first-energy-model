# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:02:51 2019

@author: Nicole
"""

import pandas as pd
import matplotlib.pyplot as plt

'''Energy generation (JXSOL Panel)'''

'Fixed Parameters'

areaPV_jxsol = 1.956*0.992 # m^2

'Variable Inputs'

efficiencyPV_jxsol = 0.18

numberPVs_jxsol = 6184

'Importing Irradiance Data and Calculating Energy Generation'

areacovered_jxsol = areaPV_jxsol*numberPVs_jxsol #m^2 (area of parking spaces covered, 12000m^2 maximum)

df1 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[9])

energygen_jxsol = efficiencyPV_jxsol*areacovered_jxsol*df1.values #kWh (W to kW conversion already done in Excel)

'Plotting the Energy Generation Profile'

plt.plot(energygen_jxsol)
plt.title('Energy Generation Over One Year')
plt.ylabel('JXSOL Energy Generation (kWh)')
plt.xlabel('Month')
plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#plt.savefig('Report/Pics_NK/energygeneration_JXSOLpanel.jpg',dpi = 1000)

#%%

'''Monthly generation'''

'Total generation in January'
jan = energygen_jxsol[:744]
total_jan = float(sum(jan))

'Total generation in February'
feb = energygen_jxsol[744:1416]
total_feb = float(sum(feb))

'Total generation in March'
mar = energygen_jxsol[1416:2160]
total_mar = float(sum(mar))

'Total generation in April'
apr = energygen_jxsol[2160:2880]
total_apr = float(sum(apr))

'Total generation in May'
may = energygen_jxsol[2880:3624]
total_may = float(sum(may))

'Total generation in June'
jun = energygen_jxsol[3624:4344]
total_jun = float(sum(jun))

'Total generation in July'
jul = energygen_jxsol[4344:5088]
total_jul = float(sum(jul))

'Total generation in August'
aug = energygen_jxsol[5088:5832]
total_aug = float(sum(aug))

'Total generation in September'
sep = energygen_jxsol[5832:6552]
total_sep = float(sum(sep))

'Total generation in October'
oct = energygen_jxsol[6552:7296]
total_oct = float(sum(oct))

'Total generation in November'
nov = energygen_jxsol[7296:8016]
total_nov = float(sum(nov))

'Total generation in December'
dec = energygen_jxsol[8016:8760]
total_dec = float(sum(dec))

'Plot monthly generation'

plt.figure()
monthlygeneration = [total_jan,total_feb,total_mar,total_apr,total_may,total_jun,total_jul,total_aug,total_sep,total_oct,total_nov,total_dec]
plt.plot(monthlygeneration)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.title('Monthly Energy Generation Over One Year')
plt.xlabel('Month')
plt.ylabel('JXSOL Energy Generation (kWh)')
plt.ylim(ymin=0)
#plt.savefig('Report/Pics_NK/energygeneration_JXSOLpanel_monthly.jpg',dpi = 1000,bbox_inches = "tight")


#%% Average hourly generation for each month of the year

'Used in total_x_kWh txt files'

print('Average hourly generation on a day in January')
jan = energygen_jxsol[:744] # 24*31 = 744 (no. values of solar_profile that correspond to Jan)
for i in range(24):
    print(float(sum(jan[i::24])/31))

print('Average hourly generation on a day in February')
feb = energygen_jxsol[744:1416]
for i in range(24):
    print(float(sum(feb[i::24])/28))
    
print('Average hourly generation on a day in March')
mar = energygen_jxsol[1416:2160]
for i in range(24):
    print(float(sum(mar[i::24])/31))

print('Average hourly generation on a day in April')
apr = energygen_jxsol[2160:2880]
for i in range(24):
    print(float(sum(apr[i::24])/30))
    
print('Average hourly generation on a day in May')
may = energygen_jxsol[2880:3624]
for i in range(24):
    print(float(sum(may[i::24])/31))
    
print('Average hourly generation on a day in June')
jun = energygen_jxsol[3624:4344]
for i in range(24):
    print(float(sum(jun[i::24])/30))
    
print('Average hourly generation on a day in July')
jul = energygen_jxsol[4344:5088]
for i in range(24):
    print(float(sum(jul[i::24])/31))
    
print('Average hourly generation on a day in August')
aug = energygen_jxsol[5088:5832]
for i in range(24):
    print(float(sum(aug[i::24])/31))
    
print('Average hourly generation on a day in September')
sep = energygen_jxsol[5832:6552]
for i in range(24):
    print(float(sum(sep[i::24])/30))
    
print('Average hourly generation on a day in October')
oct = energygen_jxsol[6552:7296]
for i in range(24):
    print(float(sum(oct[i::24])/31))
    
print('Average hourly generation on a day in November')
nov = energygen_jxsol[7296:8016]
for i in range(24):
    print(float(sum(nov[i::24])/30))
    
print('Average hourly generation on a day in December')
dec = energygen_jxsol[8016:8760]
for i in range(24):
    print(float(sum(dec[i::24])/31))