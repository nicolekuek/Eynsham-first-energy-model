# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:25:54 2018

@author: Nicole
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#%%
'''Daily electric car energy demand in November (assuming EVs are 10% of all cars)'''

#EV_data_10pc.txt file is the data from 'Second Day Trip to Pear Tree.csv' file, sheet 1, column 10
#This txt file also includes the 0 demand outside of the P&R's opening hours
time,demand = np.loadtxt('Data/EV_data_10pc.txt',delimiter = ',',unpack = True)
plt.figure()
plt.plot(time,demand)
plt.title("Daily Electric Car Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars.png', dpi = 1000)

#%%
'''Daily electric car energy demand throughout year (assuming EVs are 10% of all cars)'''

#Trafficvariation.csv file from mobility officer, Sam
traffic = pd.read_csv('Trafficvariation.csv', usecols=[0])
demand1 = demand*traffic.values/100

plt.figure()
plt.plot(time,demand1[0],label='January')
plt.plot(time,demand1[3],label='April')
plt.plot(time,demand1[6],label='July')
plt.plot(time,demand1[10],label='November')

plt.title("Daily Electric Car Energy Demand Per Season")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.legend()
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars_allmonths.png', dpi = 1000)

#%%
'''Daily electric bus energy demand'''

time,busdemand = np.loadtxt('Data/Bus_data.txt', delimiter = ',', unpack = True)
plt.figure()
plt.step(time,busdemand) # use step function, assume 1 bus every 30 mins
plt.title("Daily Electric Bus Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_busevery30mins.png', dpi = 1000)

#%% 
'''Daily EV energy demand'''

time,EVdemand = np.loadtxt('Data/Combined_data_10pc.txt', delimiter = ',', unpack = True)
plt.figure()
plt.step(time,EVdemand)
plt.title("Daily EV Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars_buses.png', dpi = 1000)

#%%
'''Annual load profile'''

monthlydemand = np.loadtxt('Data/kWh_demand_10pc.txt')
month = [0,1,2,3,4,5,6,7,8,9,10,11]
plt.figure()
plt.plot(month,monthlydemand)
plt.title("Energy Demand Over One Year")
plt.xlabel("Month")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.ylim(ymin=0)

#plt.savefig('Report/Pics_NK/energydemand_year.jpg', dpi = 1000, bbox_inches = "tight")

#%%
'''EV (10%) and electric bus energy demand throughout year using traffic variation data'''

plt.figure()

monthlydemand = np.loadtxt('Data/kWh_demand_10pc.txt')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

monthlygeneration = np.loadtxt('Data/total_monthly_kWh.txt')
plt.plot(month,monthlydemand,label='Demand')
plt.plot(month,0.5*monthlygeneration,label='50% Generation')
plt.plot(month,0.75*monthlygeneration,label='75% Generation')
plt.plot(month,monthlygeneration,label='100% Generation')

plt.ylim(ymin=0)
plt.title("Energy Demand vs Generation Over One Year")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")

plt.legend()

#%%
'''Deficit graph: solar profile - load profile for each month'''

totalnondispatchable = monthlygeneration - monthlydemand
plt.figure()
plt.plot(month,totalnondispatchable)
plt.title("Non-dispatchable asset")
plt.xlabel("Month")
plt.ylabel("Solar - Load profile (kWh)")

##%%
#'''Compare load profiles at different EV %'''
#
#x_20pc,y_20pc = np.loadtxt('Data/Combined_data_20pc.txt',delimiter = ',',unpack = True)
#x_30pc,y_30pc = np.loadtxt('Data/Combined_data_30pc.txt',delimiter = ',',unpack = True)
#
#plt.figure()
#ax = plt.subplot(1,1,1)
#p1 = plt.step(x_10pc,y_10pc,label='10% EV Load')
#p2 = plt.step(x_20pc,y_20pc,label='20% EV Load')
#p3 = plt.step(x_30pc,y_30pc,label='30% EV Load')
##p4 = plt.plot(t,jan,label='January')
##p5 = plt.plot(t,apr,label='April')
##p6 = plt.plot(t,jul,label='July')
#p7 = plt.plot(t,nov,label='Generation')
#plt.legend()
#plt.title("Effect of increasing EV usage in November")
#plt.xlabel("Time of day (hours)")
#plt.ylabel("Energy (kWh)")

#%%
'''Different EV % throughout year'''

monthlygeneration = np.loadtxt('Data/alibabageneration.txt')
month = [0,1,2,3,4,5,6,7,8,9,10,11]

plt.figure()
plt.plot(month,monthlygeneration,label='Generation')

month = [0,1,2,3,4,5,6,7,8,9,10,11]
my_xticks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.xticks(month, my_xticks)
plt.ylim(ymin=0)

plt.title("Monthly EV Demand as EV Usage Increases")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")

monthlydemand = np.loadtxt('Data/kWh_demand_10pc.txt')
plt.plot(month,monthlydemand,label='Current Demand')
plt.plot(month,1.2*monthlydemand,label='Demand (20% more EVs)')
plt.plot(month,1.5*monthlydemand,label='Demand (50% more EVs)')
plt.legend()
plt.savefig('Report/evincrease.jpg',dpi=1000,bbox_inches = "tight")