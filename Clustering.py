#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:12:28 2021

@author: mhz
"""

# Clustering
RHOB = df['RHOB']
RHOB = RHOB.to_numpy()

CNPOR = df['CNPOR']
CNPOR = CNPOR.to_numpy()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(CNPOR, RHOB, edgecolors = 'k')
plt.xlabel("Porosity (%)")
plt.ylabel("Bulk Density (g/cc)")
plt.show()