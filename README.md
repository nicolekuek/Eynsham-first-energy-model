# Eynsham (First Energy Model)

This repository contains code for the first energy model in the Eynsham P&R 3YP project.

The energy demand is based purely on Pear Tree P&R data, whereas the energy management algorithm implemented by Linh accounts for different scenarios. The energy generation and deficit remains the same for both repositories.

# Energy Demand Profiles

The first sheet of spreadsheet 'Second Day Trip to Pear Tree.xlsx contains information from Pear Tree P&R. The energy demand was calculated in Excel. Formulas can be examined by selecting the relevant cell in each column. The total energy demand was copied into the text file 'EV_data.txt' to be used in Python to plot load on an hourly basis. The electric bus demand was created assuming 50 kWh charging, 15 mins charging each time, and one bus arriving to charge every half an hour. This was then added to the electric car demand data in text file 'Combined_data.txt'.

The kWh_demand files show the monthly energy demand, accounting for traffic variation as in 'Trafficvariation.csv'.

# Energy Generation Profiles

Script pvAsset produces the final hourly energy generation profile across one year for the chosen JXSOL panel, based on averaged PVGIS solar irradiance data found in spreadsheet 'PVGIS_22deg_-5deg_2007_2016.csv'. Variables such as efficiency, losses from wiring, etc can be changed in this script to show the energy output for different scenarios.

Older versions of the energy generation profile (using Panasonic panels or with different PVGIS data) are labelled accordingly.

The 'total_xx_kwh.txt' files contain values for the hourly energy generation on a typical day in each month, obtained from these scripts. Data corresponding to monthly energy generation can also be found.

# Energy Deficit Profiles

'energydeficit_jxsol.py' provides a function to calculate and plot the hourly energy deficit across a whole year, for different numbers of solar panels installed at once.

# New Energy Model Inputs

The 'variables_for_datagen.py' script shows the trial and error process of finding the best distributions for inputs such as length of stay, state of charge, etc. These were used in Linh's algorithm.
