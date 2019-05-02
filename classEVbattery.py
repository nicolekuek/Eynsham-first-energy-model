# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 15:19:41 2019

@author: Nicole
"""

#%% Class for EV batteries to show kWh needed to fully charge

class EVbattery:
    
    def __init__(self,chargetype,capacity,SOC,lengthofstay,arrivaltime):
        self.chargetype = chargetype # determines whether fast or slow charging port
        self.capacity = capacity # kWh
        self.SOC = SOC # state of charge when arriving in P+R
        self.lengthofstay = lengthofstay # length of time car will be parked in hours (driver inputs on arrival)
        self.arrivaltime = arrivaltime # time EV arrives
        self.chargerate = (capacity - capacity*SOC)/lengthofstay # kWh if charging as soon as car parks
        
        if self.chargerate > self.chargetype:
            self.chargerate = self.chargetype #charging rate cannot be higher than rate of port