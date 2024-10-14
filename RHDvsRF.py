#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:28:22 2019

@author: Raehash
"""

import matplotlib.pyplot as plt

labels = ['Acute Rheumatic Fever with Carditis','Acute Proliferative Flomerulonephritis','Rheumatic Heart Disease', 'Acute Rheumatic Fever with Carditis and Chorea','Acute Rheumatic Fever with no heart complications', 'Acute Rheumatic Fever with Carditis']
sizes= [41,1,5,1,16,2] #percentage of each virus
explode = (0.1,0.1,0.1,0.1,0.1,0.1)

fig1,ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct= '%1.1f%%',
        pctdistance=1.2,shadow= True, labeldistance=1.5, startangle = 285)
ax1.axis('equal')
plt.title('Ratio of Heart complications after Diagnosis of Rheumatic Fever')