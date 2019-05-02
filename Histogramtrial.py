# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 16:54:47 2019

@author: Nicole
"""

#%% LENGTH OF STAY
#2nd method
#!/usr/bin/env python

import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from scipy import stats 
from scipy.stats import beta

# length of stay at car park
# car park open from 6am to 11pm (hence 17 hours max stay)
# 2.5 hours min stay (1.5 hours bus ride to city and back, 1 hour min in city)
#mu = 10 # mean of distribution
#sigma = 2.1 # standard deviation of distribution
#x = mu + sigma * np.random.randn(10000)
# 
#num_bins = 20
## the histogram of the data
#n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=1)
# 
## add a 'best fit' line
#y = mlab.normpdf(bins, mu, sigma)
#plt.figure()
#plt.plot(bins, y, 'r')
#plt.xlabel('Hours parked in P&R')
#plt.ylabel('Probability')
#plt.title('Histogram of IQ: $\mu=10$, $\sigma=2$')
# 
## Tweak spacing to prevent clipping of ylabel
#plt.subplots_adjust(left=0.15)
#plt.show()

mu = 10
sigma = 2.1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.title('Distribution representing length of stay in P&R')
plt.ylabel('Probability')
plt.xlabel('Time parked (hours)')

plt.show()

#%% EV BATTERY CAPACITY

# From report, typical capacities (all Li-ion batteries) are:

#corresponding to Renault Twizzy, Hyundai Ioniq, Nissan Leaf, VW E-Golf, Tesla Model S
capacity = [6.1,6.1,28,28,28,28,28,28,28,28,28,28,30,30,30,30,30,30,30,30,30,30,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,24.2,100,100,100]
bins = 100
plt.figure()
plt.hist(capacity, bins, normed=True, histtype='bar')

x = np.linspace(0, 120, 100) #range of kWh

## lets try the normal distribution first
#mu, sigma = stats.norm.fit(capacity) # get mean and standard deviation
#pdf_g = stats.norm.pdf(x,mu,sigma) # now get theoretical values in our interval  
#plt.plot(x, 10*pdf_g, label="Normal") # plot it
#
## gamma dist
#ag,bg,cg = stats.gamma.fit(capacity)  
#pdf_gamma = stats.gamma.pdf(x,ag,bg,cg)  
#plt.plot(x, 10*pdf_gamma, label="Gamma")

# beta dist - use this
ab,bb,cb,db = beta.fit(capacity)
pdf_beta = beta.pdf(x,ab,bb,cb,db)  
plt.plot(x, 10*pdf_beta, label="Beta")


plt.title('Distribution of popular EV battery capacities')
plt.xlabel('kWh')
plt.ylabel('Probability')
plt.legend()
plt.show()

#%% SOC on arrival

# use EV battery capacity dist
# assume majority of people coming from less than 8.6 miles away, mean 4 miles

mu = 4
sigma = 1.2
x = np.linspace(0, 10, 100)
pdf_g = stats.norm.pdf(x,mu,sigma)
plt.plot(x, pdf_g)
plt.title('Distribution representing distance travelled to P&R')
plt.ylabel('Probability')
plt.xlabel('Distance (miles)')

plt.show()

plt.figure()
consumption = 0.293 #kWh/mile
SOC = [(i - mu*consumption)/i for i in capacity] #assuming all travelling 4 miles

ab,bb,cb,db = stats.beta.fit(SOC)  
x = np.linspace(0,1,100)
pdf_beta = stats.beta.pdf(x,ab,bb,cb,db)  
plt.plot(x,pdf_beta, label="Beta")