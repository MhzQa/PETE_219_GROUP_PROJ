#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:12:10 2021

@author: mhz
"""


# Histograms


# Porosity
poro_perm_data['Porosity (%)'].plot(kind='hist', title= 'Porosity distribution')
plt.ylabel('Porosity (%)')
plt.legend(["Porosity"])
plt.show()


# Permeability
poro_perm_data['Permeability (mD)'].plot(kind='hist', title= 'Permeability distribution')
plt.ylabel('Permeability (mD)')
plt.legend(["Permeability"])