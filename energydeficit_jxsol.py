# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:58:09 2019

@author: Nicole
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##%% Energy deficit in November
#
#nov_demand = np.loadtxt('Data/Combined_data_10pc_hourly.txt')
##df = pd.read_csv('Average_daily_energy_generation.csv', usecols=[11])
#nov_generation = np.loadtxt('Data/alibabageneration_nov.txt')
#
#plt.plot(nov_demand,label='Demand')
#plt.plot(nov_generation,label='Generation')
#plt.legend()
#plt.title('Energy Demand vs Generation')
#plt.ylabel('Energy (kWh)')
#plt.xlabel('Time of Day (hours)')
#plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
##plt.savefig('Report/energy_genvsdemand_nov.png',dpi = 1000)
#
#'Non-Dispatchable energy'
#nondispatchable = nov_generation - nov_demand
#plt.figure()
#plt.plot(nondispatchable)

#%% Energy deficit over year

def energydeficit(numberPVs,efficiencyPV,proportionEVs):
 
    areaPV = 1.956*0.992 # m^2
    areacovered = areaPV*numberPVs #m^2 (area of parking spaces covered, 12000m^2 maximum)
    pv_losses = 0.14
    df1 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[9])
    energygeneration = efficiencyPV*areacovered*(1-pv_losses)*df1.values #kWh
    
    #max number of PVs is 4995
    
    df2 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[10]) #electric car demand
    df3 = pd.read_csv('PVGIS_22deg_-5deg_2007_2016.csv', usecols=[11]) #electric bus demand
    energydemand = proportionEVs*10*df2.values + df3.values #kWh
    
    #proportion of EVs relative to total car park users assumed to be 10% for first phase
    
    energydeficit = energygeneration - energydemand #kWh
    
    plt.plot(energydeficit,label=numberPVs)
    plt.title('Difference in Energy Generation and Demand')
    plt.ylabel('Energy Generation - Demand (kWh)')
    plt.xlabel('Month')
    plt.xticks([0,744,1416,2160,2880,3624,4344,5088,5832,6552,7296,8016],['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    plt.legend(title = 'No. panels installed')
    
energydeficit(4995,0.18,0.1)
energydeficit(3750,0.18,0.1)
energydeficit(2500,0.18,0.1)
plt.savefig('Report/Pics_NK/nondispatchable_year.jpg',dpi = 1000)