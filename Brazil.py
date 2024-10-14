#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:30:30 2019

@author: Raehash
"""
import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25

 
# set height of bar
bars1 = [5.0, 15.0, 12.5, 15.0, 22.5,22.5,57.5,12.5,2.5,0.0,35]
bars2 = [22.0,26.0, 24.0, 23.0, 38.0,18.0,26.3,2.5,0.0,0.0,27.5]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Rheumatic Fever')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Control')
 
# Add xticks on the middle of the group bars
plt.xlabel('HLA Types', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['DR1', 'DR2', 'DR3', 'DR4', 'DR5','DRw6','DR7','DRw8','DRw9','DRw10','DRblank'],rotation = 45)
 
plt.ylabel('Percentage of Sample')

plt.title('Brazillian HLA Types in patients with Rheumatic Fever')
# Create legend & Show graphic
plt.legend()
plt.show()

