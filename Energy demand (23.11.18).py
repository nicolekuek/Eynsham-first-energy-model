# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:07:35 2018

@author: Nicole
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:

# using txt file data - updated with 2nd pear tree visit data
'''10% EVs - using Peartree November data'''
x1,y1 = np.loadtxt('EV_data_10pc.txt',delimiter = ',',unpack = True)
plt.plot(x1,y1)
plt.title("Daily EV energy demand (10% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[3]:

# using txt file data - updated with 2nd pear tree visit data
'''20% EVs - using Peartree November data, same distribution but double energy needed'''
x1,y1 = np.loadtxt('EV_data_10pc.txt',delimiter = ',',unpack = True)
plt.plot(x1,2*y1)
plt.title("Daily EV energy demand (20% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[4]:

'''10% EVs - showing changes in traffic throughout year
Using mobility data, taking November as a base and comparing others to it'''
x1,y1 = np.loadtxt('EV_data_10pc.txt',delimiter = ',',unpack = True)
p1 = plt.plot(x1,0.9082787386*y1,label='January load')
p2 = plt.plot(x1,0.9834519438*y1,label='February load')
p3 = plt.plot(x1,1.021061823*y1,label='March load')
p4 = plt.plot(x1,1.033639737*y1,label='April load')
p5 = plt.plot(x1,1.024820255*y1,label='May load')
p6 = plt.plot(x1,1.043643152*y1,label='June load')
p7 = plt.plot(x1,1.060335362*y1,label='July load')
p8 = plt.plot(x1,1.01859683*y1,label='August load')
p9 = plt.plot(x1,1.029020244*y1,label='September load')
p10 = plt.plot(x1,1.029978241*y1,label='October load')
p11 = plt.plot(x1,y1,label='November load')
p12 = plt.plot(x1,0.9082021647*y1,label='December load')
plt.title("Daily EV energy demand throughout year")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")
plt.legend()


# In[5]:

# using txt file data
x2,y2 = np.loadtxt('Bus_data.txt', delimiter = ',', unpack = True)
plt.step(x2,y2) # use step function - check bus charging times are right in txt file
plt.title("Daily electric bus energy demand")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[6]:

'''Combined 10% EV and electric bus energy demand'''
x_10pc,y_10pc = np.loadtxt('Combined_data_10pc.txt', delimiter = ',', unpack = True)
plt.step(x_10pc,y_10pc)
plt.title("Daily November electric bus and vehicle energy demand (10% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[7]:

'''Combined 20% EV and electric bus energy demand'''
x_20pc,y_20pc = np.loadtxt('Combined_data_20pc.txt', delimiter = ',', unpack = True)
plt.step(x_20pc,y_20pc)
plt.title("Daily November electric bus and vehicle energy demand (20% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[8]:

'''Combined 30% EV and electric bus energy demand'''
x_30pc,y_30pc = np.loadtxt('Combined_data_30pc.txt', delimiter = ',', unpack = True)
plt.step(x_30pc,y_30pc)
plt.title("Daily November electric bus and vehicle energy demand (30% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")

# In[9]:

'''Load and plot average daily solar profile for all months'''
jan2016_data = pd.read_csv('solarJan2016.csv', usecols=[13])
feb2016_data = pd.read_csv('solarFeb2016.csv', usecols=[13])
mar2016_data = pd.read_csv('solarMar2016.csv', usecols=[13])
apr2016_data = pd.read_csv('solarApr2016.csv', usecols=[13])
may2016_data = pd.read_csv('solarMay2016.csv', usecols=[13])
jun2016_data = pd.read_csv('solarJun2016.csv', usecols=[13])
jul2016_data = pd.read_csv('solarJul2016.csv', usecols=[13])
aug2016_data = pd.read_csv('solarAug2016.csv', usecols=[13])
sep2016_data = pd.read_csv('solarSep2016.csv', usecols=[13])
oct2016_data = pd.read_csv('solarOct2016.csv', usecols=[13])
nov2016_data = pd.read_csv('solarNov2016.csv', usecols=[13])
dec2016_data = pd.read_csv('solarDec2016.csv', usecols=[13])

# In[10]:

'''Total kWh in 2016 assuming 15% efficiency'''
jan2016_data = pd.read_csv('solarJan2016.csv', usecols=[13])

# In[11]:

'''Plot of Nov solar and load profiles with 10% EVs'''
ax = plt.subplot(1,1,1)
p1 = plt.step(x_10pc,y_10pc,label='Load')
p2 = plt.plot(nov2016_data,label='Solar')
plt.legend()
plt.title("Comparison of November solar and load profiles (10% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")
#plt.plot(p1-p2)
#convert to array and subtract
#np.zeros(n,1)


# In[ ]:

'''Difference between load and november solar for 10% EVs'''
#subtract (not p1 and p2 since those are lists)

# In[ ]:


'''Plot of Nov solar and load profiles with 20% EVs'''
ax = plt.subplot(1,1,1)
p1 = plt.step(x_20pc,y_20pc,label='Load')
p2 = plt.plot(nov2016_data,label='Solar')
plt.legend()
plt.title("Comparison of November solar and load profiles (20% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[ ]:


'''Difference between load and november solar for 20% EVs'''


# In[ ]:


'''Plot of Nov solar and load profiles with 30% EVs'''
ax = plt.subplot(1,1,1)
p1 = plt.step(x_30pc,y_30pc,label='Load')
p2 = plt.plot(nov2016_data,label='Solar')
plt.legend()
plt.title("Comparison of November solar and load profiles (30% EVs)")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[ ]:


'''Difference between load and november solar for 30% EVs'''


# In[ ]:


'''Compare load profiles at different EV %'''
ax = plt.subplot(1,1,1)
p1 = plt.step(x_10pc,y_10pc,label='10% EV Load')
p2 = plt.step(x_20pc,y_20pc,label='20% EV Load')
p3 = plt.step(x_30pc,y_30pc,label='30% EV Load')
p4 = plt.plot(nov2016_data,label='November solar')
plt.legend()
plt.title("Effect of increasing EV usage in November")
plt.xlabel("Time of day (hours)")
plt.ylabel("Energy (kWh)")


# In[ ]:

'''Calculation of total kWh generated over year from PVGIS data assuming 15% efficiency'''




# In[ ]:

'''Plot of total kWh generated over first year (sum total kWh each month and plot)'''



# In[ ]:




