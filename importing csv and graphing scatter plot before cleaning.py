#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:04:01 2021

@author: mhz
"""

#STEP 1: install csv and clean data
import pandas as pd 
poro_perm_data = pd.read_csv('poro_perm_data.csv')
poro_perm_data.head()
poro_perm_data.columns # shows column labels as series
#poro_perm_data not cleaning raw data

#for null values
poro_perm_data.dropna(axis = 0, inplace = True)
poro_perm_data.isnull().sum()
#after cleaning null values only

import matplotlib.pyplot as plt

#for null values
poro_perm_data.dropna(axis = 0, inplace = True)
poro_perm_data.isnull().sum() #after cleaning Facies null values

import matplotlib.pyplot as plt
fig1 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'Depth Vs. Porosity')
plt.legend(['Depth (ft)','Porosity (%)'])
fig2 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'permeability (mD)', color='black', title= 'Depth Vs. Permeability')
plt.legend(['Depth (ft)','Permeability (mD)'])

#line data is canceled because it is too complicated and useless
#plt.plot(data['Depth (ft)'], data['Porosity (%)'],linestyle='-', color='blue', linewidth=2, alpha=1)

#identify null value by true, and by table
bool1 = poro_perm_data.loc[:,"Facies"].isnull()
null_preveious_rank = poro_perm_data.loc[bool1]
null_preveious_rank

poro_perm_data.describe()
