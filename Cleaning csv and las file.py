#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:10:29 2021

@author: mhz
"""

# Cleaning the csv and las files

# No more 100000 or negative values are in the data
# Cleaning las file
import numpy as np
df = df.replace(0, np.nan)
df = df.dropna(how = 'all', axis = 0)
df = df.replace(np.nan, 0)
df = df.drop(columns = 'AVTX')
df = df.drop(columns = 'BVTX')
df = df.drop(columns = 'LSPD')
df = df.drop(columns = 'SP')
df = df.drop(columns = 'ITT')
df = df[df['CILD'] > 0]
df = df[df['CNDL'] > 0]
df = df[df['CNLS'] > 0]
df = df[df['CNPOR'] > 0]
df = df[df['CNSS'] > 0]
df = df[df['GR'] > 0]
df = df[df['LTEN'] > 0]
df = df[df['RILD'] != 100000]
df = df[df['RILM'] > 0]
df = df[df['RLL3'] > 0]
df = df[df['RXORT'] > 0]
df = df[df['MCAL'] > 0]
df = df[df['MI'] > 0]
df = df[df['MN'] > 0]
df = df[df['DT'] > 0]
df = df[df['SPOR'] > 0]
df = df[df['DCAL'] > 0]
df = df[df['RHOB'] > 0]
df = df[df['RHOC'] > 0]
df = df[df['DPOR'] > 0]
df = df.reset_index()
df = df.rename(columns = {'DEPT' : 'DEPTH'}) # Renaming the column DEPT to DEPTH
df = df.drop([1258,1]) #[there is one point in RHOB that can be considered as an outlier therefore it can be removed]
summary = df.describe() # Summary of the data after it's cleaned to check the values



# Cleaning the csv file
import numpy as np
d = poro_perm_data.replace(0, np.nan)
d = poro_perm_data.dropna(how = 'all', axis = 0)
d = poro_perm_data.replace(np.nan, 0)

#  deletes all the values below zero in porosity csv file
poro_perm_data = poro_perm_data[poro_perm_data['Porosity (%)'] > 0]

#  deletes all the values below zero in permeability csv file
poro_perm_data = poro_perm_data[poro_perm_data['Permeability (mD)'] > 0]