#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:11:35 2021

@author: mhz
"""

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