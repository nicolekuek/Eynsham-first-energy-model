# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 19:25:54 2018

@author: Nicole
"""
import matplotlib.pyplot as plt
import numpy as np

#%%
'''Daily electric car (10%) energy demand in November'''

x1,y1 = np.loadtxt('Data/EV_data_10pc.txt',delimiter = ',',unpack = True)
plt.figure()
plt.step(x1,y1)
plt.title("Daily Electric Car Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars.png', dpi = 1000)

#%%
'''Daily electric car (10%) energy demand throughout year'''

plt.figure()
x1,y1 = np.loadtxt('Data/EV_data_10pc.txt',delimiter = ',',unpack = True)
p1 = plt.plot(x1,0.9082787386*y1,label='January')
#p2 = plt.plot(x1,0.9834519438*y1,label='February')
#p3 = plt.plot(x1,1.021061823*y1,label='March')
p4 = plt.plot(x1,1.033639737*y1,label='April')
#p5 = plt.plot(x1,1.024820255*y1,label='May')
#p6 = plt.plot(x1,1.043643152*y1,label='June')
p7 = plt.plot(x1,1.060335362*y1,label='July')
#p8 = plt.plot(x1,1.01859683*y1,label='August')
#p9 = plt.plot(x1,1.029020244*y1,label='September')
#p10 = plt.plot(x1,1.029978241*y1,label='October')
p11 = plt.plot(x1,y1,label='November')
#p12 = plt.plot(x1,0.9082021647*y1,label='December')
plt.title("Daily Electric Car Energy Demand Throughout Year")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.legend()
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars_allmonths.png', dpi = 1000)
plt.legend()   

#%%
'''Daily electric bus energy demand'''

x2,y2 = np.loadtxt('Data/Bus_data.txt', delimiter = ',', unpack = True)
plt.figure()
plt.step(x2,y2) # use step function - check bus charging times are right in txt file
plt.title("Daily Electric Bus Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_busevery30mins.png', dpi = 1000)

#%% 
'''Daily EV energy demand'''

x_10pc,y_10pc = np.loadtxt('Data/Combined_data_10pc.txt', delimiter = ',', unpack = True)
plt.figure()
plt.step(x_10pc,y_10pc)
plt.title("Daily EV Energy Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy Demand (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydemand_oneday_10pc_cars_buses.png', dpi = 1000)

#%%
'''Daily solar profiles at 19.7% efficiency'''

jan = np.loadtxt('Data/total_01_kWh.txt')
feb = np.loadtxt('Data/total_02_kWh.txt')
mar = np.loadtxt('Data/total_03_kWh.txt')
apr = np.loadtxt('Data/total_04_kWh.txt')
may = np.loadtxt('Data/total_05_kWh.txt')
jun = np.loadtxt('Data/total_06_kWh.txt')
jul = np.loadtxt('Data/total_07_kWh.txt')
aug = np.loadtxt('Data/total_08_kWh.txt')
sep = np.loadtxt('Data/total_09_kWh.txt')
oct = np.loadtxt('Data/total_10_kWh.txt')
nov = np.loadtxt('Data/total_11_kWh.txt')
dec = np.loadtxt('Data/total_12_kWh.txt')

#%%
'''November solar and load profiles'''

t = range(0,25)

plt.figure()
plt.step(x_10pc,y_10pc,label='Energy Demand')
plt.plot(t,nov,label='Energy Generation')
plt.title("November Generation vs Demand")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Energy (kWh)")
plt.legend()
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/generationvsdemand_nov.png', dpi = 1000)

'''November deficit: solar - load'''

t,nov_nondispatchable = np.loadtxt('Data/112016_kWh_nondispatchable.txt', delimiter = ',', unpack = True)
plt.figure()
plt.step(t,nov_nondispatchable)
plt.title("Non-Dispatchable Asset")
plt.xlabel("Time of Day (hours)")
plt.ylabel("Excess Energy (kWh)")
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
#plt.savefig('Report/energydeficit_nov.png', dpi = 1000)

#%%
'''Solar and load profiles throughout year'''

t = range(0,25)

plt.figure()
plt.step(x_10pc,y_10pc,label='Demand')
plt.plot(t,jan,label='January')
#plt.plot(t,feb,label='February')
#plt.plot(t,mar,label='March')
plt.plot(t,apr,label='April')
#plt.plot(t,may,label='May')
#plt.plot(t,jun,label='June')
plt.plot(t,jul,label='July')
#plt.plot(t,aug,label='August')
#plt.plot(t,sep,label='September')
#plt.plot(t,oct,label='October')
plt.plot(t,nov,label='November')
#plt.plot(t,dec,label='December')
plt.title("Daily energy demand vs generation (using max PVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")
plt.legend()

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

#plt.savefig('Report/energydeficit_nov.png', dpi = 1000)

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

#%%
'''Compare load profiles at different EV %'''

x_20pc,y_20pc = np.loadtxt('Data/Combined_data_20pc.txt',delimiter = ',',unpack = True)
x_30pc,y_30pc = np.loadtxt('Data/Combined_data_30pc.txt',delimiter = ',',unpack = True)

plt.figure()
ax = plt.subplot(1,1,1)
p1 = plt.step(x_10pc,y_10pc,label='10% EV Load')
p2 = plt.step(x_20pc,y_20pc,label='20% EV Load')
p3 = plt.step(x_30pc,y_30pc,label='30% EV Load')
#p4 = plt.plot(t,jan,label='January')
#p5 = plt.plot(t,apr,label='April')
#p6 = plt.plot(t,jul,label='July')
p7 = plt.plot(t,nov,label='Generation')
plt.legend()
plt.title("Effect of increasing EV usage in November")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")

#%%
'''Different EV % throughout year'''

monthlygeneration = np.loadtxt('Data/total_monthly_kWh.txt')
month = [0,1,2,3,4,5,6,7,8,9,10,11]

plt.figure()
plt.plot(month,monthlygeneration,label='Generation')

month = [0,1,2,3,4,5,6,7,8,9,10,11]
my_xticks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.xticks(month, my_xticks)
plt.ylim(ymin=0)

plt.title("Effect of increasing EV usage")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")

monthlydemand = np.loadtxt('Data/kWh_demand_10pc.txt')
plt.plot(month,monthlydemand,label='Demand (10% EVs)')

monthlydemand = np.loadtxt('Data/kWh_demand_20pc.txt')
plt.plot(month,monthlydemand,label='Demand (20% EVs)')

monthlydemand = np.loadtxt('Data/kWh_demand_30pc.txt')
plt.plot(month,monthlydemand,label='Demand (30% EVs)')
plt.legend()

'''Including 22 160W lights'''
plt.figure()
monthlygeneration = np.loadtxt('Data/total_monthly_kWh.txt')
month = [1,2,3,4,5,6,7,8,9,10,11,12]
plt.plot(month,monthlygeneration,label='Generation')
monthlydemand = np.loadtxt('Data/kWh_demand_10pc_withlighting.txt')
plt.plot(month,monthlydemand)
plt.title('Annual generation vs demand (including lighting demand)')
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.legend()

'''Begbroke Science Park'''
plt.figure()
monthlygeneration = np.loadtxt('Data/total_monthly_kWh.txt')
month = [1,2,3,4,5,6,7,8,9,10,11,12]
my_xticks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.xticks(month, my_xticks)
plt.plot(month,monthlygeneration,label='Generation')
monthlydemand = np.loadtxt('Data/Begbroke.txt')
plt.plot(month,monthlydemand,label='Demand')

plt.ylim(ymin=0)
plt.title('Annual generation vs Begbroke demand')
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.legend()