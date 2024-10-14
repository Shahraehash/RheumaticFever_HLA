#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:54:54 2019

@author: Raehash
"""

import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25

 
# set height of bar
bars1 = [21.5,12.9,21.5,37.6,9.7,32.2,33.3,4.3]
bars2 = [25.0,16.2,23.7,7.5,15.0,18.7,21.2,11.2]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Rheumatic Fever')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Control')
 
# Add xticks on the middle of the group bars
plt.xlabel('HLA Types', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['DR1', 'DR2', 'DR3', 'DR4', 'DR5','DR7','DRw52','DRw53'],rotation = 45)
 
plt.ylabel('Percentage of Sample')

plt.title('Turkish HLA Types in patients with Rheumatic Fever')
# Create legend & Show graphic
plt.legend()
plt.show()
