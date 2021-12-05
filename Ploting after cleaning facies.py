#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:09:33 2021

@author: mhz
"""

#now min and max of each facies is identified
#-----------------------------------------------------------------------

#plots for channel 
fig3 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'Channel facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig4 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'Channel facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])

#plots for crevasse splay 
fig5 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'crevasse splay facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig6 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'crevasse splay facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])

#plots for overbanks
fig7 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'overbanks facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig8 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'overbanks facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])
