#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 13:08:14 2021

@author: mhz
"""

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