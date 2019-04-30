# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:54:47 2019

@author: Nicole
"""

#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

'''This script experiments with different distributions
    from which Linh's algorithm samples'''

#%% LENGTH OF STAY
#2nd method

mu = 10

'Trialling different sigma values'

for sigma in [0.5,1.8,2.5,3]:
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma),label = sigma)
    plt.title('Length of Stay in P&R')
    plt.ylabel('Probability')
    plt.xlabel('Time Parked (Hours)')
    plt.legend()
#    plt.savefig('Report/lengthofstay_sigmas.png', dpi = 1000)

'Final distribution'

sigma = 2.1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.figure()
plt.plot(x, stats.norm.pdf(x, mu, sigma), label = sigma)
plt.title('Length of Stay in P&R')
plt.ylabel('Probability')
plt.xlabel('Time Parked (Hours)')
plt.legend()
#plt.savefig('Report/lengthofstay.png', dpi = 1000)

'Random sample from distribution'

time = np.random.normal(10,2.1)
print(time)

#%% CHARGING TYPE 

'Use the random sample for length of stay to predict charge type'

if time > 4:
    ctype = 0 #slow charging takes 8 hours to charge from flat to full
else:
    ctype = 1 #fast charging takes 4 hours to charge from flat to full


#%% EV BATTERY CAPACITY

'Frequency of electric car battery capacities'
#corresponding to Renault Twizzy, Hyundai Ioniq, Nissan Leaf, VW E-Golf, Tesla Model S
capacity = [6.1,6.1,28,28,28,28,28,28,28,28,28,28,30,30,30,30,30,30,30,30,30,30,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,100,100,100]
bins = 100
plt.figure()
fig = plt.hist(capacity, bins, normed=True, histtype='bar')

x = np.linspace(0, 120, 100) #range of kWh 

'Normal distribution trial'
mu, sigma = stats.norm.fit(capacity) # get mean and standard deviation
pdf_g = stats.norm.pdf(x,mu,sigma) # now get theoretical values in our interval  
plt.plot(x, 10*pdf_g, label="Normal") # plot it

'Gamma distribution trial (this turns out to be the best fit)'
ag,bg,cg = stats.gamma.fit(capacity)  
pdf_gamma = stats.gamma.pdf(x,ag,bg,cg)  
plt.plot(x, 10*pdf_gamma,label="Gamma")

'Beta distribution trial'
ab,bb,cb,db = stats.beta.fit(capacity)  
pdf_beta = stats.beta.pdf(x,ab,bb,cb,db)  
plt.plot(x, 10*pdf_beta, label="Beta")

'Plot (and compare) distributions against histogram'

plt.title('Electric Car Battery Capacity')
plt.xlabel('Capacity (kWh)')
plt.ylabel('Probability')
plt.legend(title='Distribution Type')
#plt.savefig('Report/Pics_NK/capacity.jpg',dpi = 1000)

'Create gamma distribution similar to that which was fitted to the histogram'

# mu = 32kWh from Sam's data
# shape = sqrt(mu), scale = shape
shape, scale = 5.66,7

# Print 100 samples to check random nature
for i in range (0,100):
    s = np.random.gamma(shape, scale)
    print(s)

# Plot distribution
plt.figure()
import scipy.special as sps
s = np.random.gamma(shape, scale,1000)
count, bins, ignored = plt.hist(s, 50, density=True)
y = bins**(shape-1)*(np.exp(-bins/scale) /
                     (sps.gamma(shape)*scale**shape))
plt.plot(bins, y, linewidth=2, color='r')
plt.title('Electric Car Battery Capacity')
plt.xlabel('Capacity (kWh)')
plt.ylabel('Probability')
#plt.legend()
#plt.savefig('Report/capacity_final.png',dpi = 1000)

'Random sample'

capacity = np.random.gamma(shape, scale)

#%% SOC on arrival

'Use EV battery capacity distribution - did not work'

from scipy.stats import beta

a, b = 2, 1.7
mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')

plt.figure()
x = np.linspace(beta.ppf(0.01, a, b),
                beta.ppf(0.99, a, b), 100)
plt.plot(x, beta.pdf(x, a, b),
       'r-', lw=5, alpha=0.6, label='beta pdf')
plt.title('State of Charge')
plt.xlabel('Proportion of full charge on arrival (i.e. SOC)')
plt.ylabel('Probability')
#plt.savefig('Report/soc.png',dpi=1000)

# Print 100 samples to check random nature
for i in range (0,100):
    SOC = np.random.beta(a,b)
    print(SOC)

SOC = np.random.beta(a,b)

#%% Arrival time

'Import and plot arrival data from Pear Tree csv'

df = pd.read_csv('Arrivaltime.csv', usecols=[1])
totalcars = 617
arrival = df.values/totalcars
plt.figure()
plt.plot(arrival,label='Pear Tree Data')
plt.xticks([0,4,8,12,16,20,24],['00:00','04:00','08:00','12:00','16:00','20:00','00:00'])
plt.title('Arrival Time')
plt.xlabel('Time of Day (hours)')
plt.ylabel('Probability')
plt.legend()

'Approximate Pear Tree distribution using a mixture of normal distributions'
# trialled different sigmas

import seaborn as sns
n = 10000 # number of samples to be drawn
mu = [9, 17] # mean of each normal distribution (i.e. the peaks)
sigma = [0.1,2.1] # standard deviation of each dist which allows best fit of Pear Tree data
samples = []
for i in range(n): # iteratively draw samples
    Z = np.random.choice([0,1]) # latent variable
    samples.append(np.random.normal(mu[Z], sigma[Z], 1))
sns_plot = sns.distplot(samples, hist=False, label=sigma) # compare plot with Pear Tree
plt.show()
fig = sns_plot.get_figure()
#fig.savefig('Report/Pics_NK/arrivaltime.jpg',dpi = 1000)

'Random sample'

n = 1 # extract one sample
mu = [9, 17]
sigma = [0.1,2.1]
Z = np.random.choice([0,1]) # latent variable
arrivaltime = float(np.random.normal(mu[Z], sigma[Z], 1))
print(arrivaltime)