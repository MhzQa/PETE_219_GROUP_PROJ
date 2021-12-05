#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:11:56 2021

@author: omarhussein
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


#----------------------------------------------------------------------
#STEP 2: install las and clean data
import lasio
f = open('1051661435.las', 'r') # 'r' = read
lines = f.read()

#f and lines are the las file
las = lasio.read('1051661435.las')
data = pd.read_csv('poro_perm_data.csv')
df = las.df()
data.isnull().sum()
# gr = df.describe()


bool_las = (poro_perm_data.loc[: ,"Permeability (mD)"] <=0) & (poro_perm_data.loc[: ,"Porosity (%)"] <=0)
newlasdata = poro_perm_data[bool_las]
newlasdata.shape

bool_las = poro_perm_data.loc[:,"Facies"] == "'overbanks'"
newOdata= poro_perm_data[bool_las]
newOdata.describe()

bool_las2 = poro_perm_data.loc[:,"Facies"] == "'crevasse splay'"
newCdata= poro_perm_data[bool_las2]
newCdata.describe()

bool_las3 = poro_perm_data.loc[:,"Facies"] == "'channel'"
newCHdata= poro_perm_data[bool_las3]
newCHdata.describe()

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

#-----------------------------------------------------------------------

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

#-----------------------------------------------------------------------


# Well Logs 
# Deep
ax = df.plot(x='RILD', y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(228.5, 4556)
plt.xlim(0,350)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Deep Resistivity Measurements')
ax.set_xlabel("RILD")
ax.xaxis.set_label_position('top')

#Medium
#Medium
bx = df.plot(x='RILM', y='DEPTH', c='green', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(228.5, 4456)
plt.xlim(0,150)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Medium Resistivity Measurements')
bx.set_xlabel("RILM")
bx.xaxis.set_label_position('top')

#Shallow
cx = df.plot(x='RLL3', y='DEPTH', c='blue', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(228.5, 4456)
plt.xlim(0,160)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Shallow Resistivity Measurements')
cx.set_xlabel("RLL3")
cx.xaxis.set_label_position('top')

#logs all together
ax = df.plot(x='RILD', y='DEPTH', c='blue', lw=0.5, legend=False, figsize=(7,10))
ax = df.plot(x='RLL3', y='DEPTH', c='red', lw=0.5, legend=False, figsize=(7,10),ax=ax)
ax = df.plot(x='RILM', y='DEPTH', c='green', lw=0.5, legend=False, figsize=(7,10), ax=ax)
plt.ylim(300, 5000)
plt.xlim(0,400)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('RILM, RILD, RLL3')
ax.set_xlabel("RILM, RILD, RLL3 (ohm.m)")
ax.xaxis.set_label_position('top') 
plt.show()

# The bulk density plot final form
# Plot of bulk density adapted with a color map fill
left_col_value = 1.4
right_col_value = 2.8
# assign the column to a variable for easier reading
curve = df['RHOB']
# calculate the span of values
span = abs(left_col_value - right_col_value)
# assign a color map
cmap = plt.get_cmap('autumn_r')
# create array of values to divide up the area under curve
color_index = np.arange(left_col_value, right_col_value, span / 100)
# setup the plot
ax = df.plot(x='RHOB', y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(4456, 228.5)
plt.xlim(1.4,2.8)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Bulk Density')
ax.set_xlabel("RHOB")
ax.xaxis.set_label_position('top')
for index in sorted(color_index):
    index_value = (index - left_col_value)/span
    color = cmap(index_value) #obtain colour for color index value
    plt.fill_betweenx(df['DEPTH'], 400 , curve, where = curve >= index,  color = color)
plt.show()


# Gamma Ray Color Map
# Plot of Gamma ray adapted with a color map fill
left_col_value = 12.8
right_col_value = 203
# assign the column to a variable for easier reading
curve = df['GR']
# calculate the span of values
span = abs(left_col_value - right_col_value)
# assign a color map
cmap = plt.get_cmap('viridis')
# create array of values to divide up the area under curve
color_index = np.arange(left_col_value, right_col_value, span / 100)
# setup the plot
ax = df.plot(x='GR', y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(4456, 228.5)
plt.xlim(12.8,203)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Gamma Ray')
ax.set_xlabel("GR")
ax.xaxis.set_label_position('top')
for index in sorted(color_index):
    index_value = (index - left_col_value)/span
    color = cmap(index_value) #obtain colour for color index value
    plt.fill_betweenx(df['DEPTH'], 400 , curve, where = curve >= index,  color = color)
plt.show()

#-----------------------------------------------------------------------


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

#-----------------------------------------------------------------------

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


#-----------------------------------------------------------------------
    
# Density and porosity because no neutron, but it has a color map
fig = plt.subplots(figsize=(7,10))

ax1 = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan=1)
ax2 = ax1.twiny()

ax1.plot('RHOB', 'DEPTH', data=df, color='red', lw=0.5)
ax1.set_xlim(1.44, 2.8)
ax1.set_xlabel('Density')
ax1.xaxis.label.set_color("red")
ax1.tick_params(axis='x', colors="red")
ax1.spines["top"].set_edgecolor("red")

ax2.plot('CNPOR', 'DEPTH', data=df, color='blue', lw=0.5)
ax2.set_xlim(58, 1.6)
ax2.set_xlabel('Porosity (%)')
ax2.xaxis.label.set_color("blue")
ax2.spines["top"].set_position(("axes", 1.08))
ax2.tick_params(axis='x', colors="blue")
ax2.spines["top"].set_edgecolor("blue")

x1=df['RHOB']
x2=df['CNPOR']

x = np.array(ax1.get_xlim())
z = np.array(ax2.get_xlim())

nz=((x2-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

ax1.fill_betweenx(df['DEPTH'], x1, nz, where=x1>=nz, interpolate=True, color='green')
ax1.fill_betweenx(df['DEPTH'], x1, nz, where=x1<=nz, interpolate=True, color='yellow')

for ax in [ax1, ax2]:
    ax.set_ylim(4400, 2500)
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")


