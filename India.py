#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:51:21 2019

@author: Raehash
"""

import numpy as np
import matplotlib.pyplot as plt
 
# set width of bar
barWidth = 0.25

 
# set height of bar
bars1 = [21.82, 21.82, 50.00, 18.18, 17.27,13.63,24.45,1.32,2.73]
bars2 = [14.17, 47.02, 26.12, 26.12, 23.13,17.91,22.38,0.74,2.78]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='Rheumatic Fever')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='Control')
 
# Add xticks on the middle of the group bars
plt.xlabel('HLA Types', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['DR1', 'DR2', 'DR3', 'DR4', 'DR5','DRw6','DR7','DRw8','DRw9'],rotation = 45)
 
plt.ylabel('Percentage of Sample')

plt.title('Indian HLA Types in patients with Rheumatic Fever')
# Create legend & Show graphic
plt.legend()
plt.show()
