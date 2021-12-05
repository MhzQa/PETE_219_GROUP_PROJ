#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:11:03 2021

@author: mhz
"""

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