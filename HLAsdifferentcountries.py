#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:43:02 2019

@author: Raehash
"""
import pandas as pd
import matplotlib.pyplot as plt

raw_data= {'Country': ['Brazil', 'India', 'Turkey'],
            'HLA-DR1': [4,14,15],
            'HLA-DR2': [12,14,10],
            'HLA-DR3': [10,33,15],
            'HLA-DR4': [12,12,28],
            'HLA-DR5': [17,11,8],
            'HLA-DR7': [45,16,24]} #percent of that order of the virus exists

           
           
rs = pd.DataFrame.from_dict(raw_data, 
                            #columns = ['HLA-DR1', 'HLA-DR2', 'HLA-DR3', 'HLA-DR4', 'HLA-DR5', 'HLA-DR7', 'Corynebacterium_phage', 'Other']
                            )
sum(raw_data['HLA-DR1'])
sum(raw_data['HLA-DR2'])
sum(raw_data['HLA-DR3'])
sum(raw_data['HLA-DR4'])
sum(raw_data['HLA-DR5'])
sum(raw_data['HLA-DR7'])



numbers=[sum(raw_data['HLA-DR1']),
sum(raw_data['HLA-DR2']),
sum(raw_data['HLA-DR3']),
sum(raw_data['HLA-DR4']),
sum(raw_data['HLA-DR5']),
sum(raw_data['HLA-DR7'])]

total=sum(numbers)

B = ['Brazil','India','Turkey']


Pseudomonas_per=(sum(raw_data['HLA-DR1'])/total)*100

Bacillus_per=(sum(raw_data['HLA-DR2'])/total)*100

Rhodococcus_per=(sum(raw_data['HLA-DR3'])/total)*100

Propionibacterium_per=(sum(raw_data['HLA-DR4'])/total)*100

Planktothrix_per=(sum(raw_data['HLA-DR5'])/total)*100

Staphylococcus_per=(sum(raw_data['HLA-DR7'])/total)*100


f, ax1 = plt.subplots(1, figsize=(10,5))
bar_width =0.25
bar_l = [i+1 for i in range (len(rs['HLA-DR1']))]
tick_pos = [i+(bar_width/2) for i in bar_l]
ax1.bar(bar_l,
    rs['HLA-DR1'],
        # set the width
    width=bar_width,
        # with the label Pseudimonas phage
    label='HLA-DR1',
        # with alpha 0.5
    alpha=0.75,
        # with color
    color='#191970')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the Bacillus phage
    rs['HLA-DR2'],
        # set the width
    width=bar_width,
        # with Pseudimonas phage on the bottom
    bottom=rs['HLA-DR1'],
        # with the label Bacillus phage
        label='HLA-DR2',
        # with alpha 0.5
    alpha=0.75,
        # with color
        color='#FF8C00')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the Rhodococcus phage data
    rs['HLA-DR3'],
        # set the width
    width=bar_width,
        # with Pseudomonas phage and Bacillus phage on the bottom
    bottom=[i+j for i,j in zip(rs['HLA-DR1'],rs['HLA-DR2'])],
        # with the label Rhodococcus phage
    label='HLA-DR3',
        # with alpha 0.5
    alpha=0.75,
        # with color
    color='#006400')
            
# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the Propionibacterium phage
    rs['HLA-DR4'],
        # set the width
    width=bar_width,
        # with Pseudomonas phage and Bacillus phage and Rhodococcus phage on the bottom
    bottom=[i+j+k for i,j,k in zip(rs['HLA-DR1'],rs['HLA-DR2'], rs['HLA-DR3'])],
        # with the label post score
    label='HLA-DR4',
        # with alpha 0.5
    alpha=0.75,
        # with color
    color='#8B0000')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the Planktothrix phage
    rs['HLA-DR5'],
        # set the width
    width=bar_width,
        # with Pseudomonas phage and Bacillus phage and Rhodococcus phage and Propionibacterium phage on the bottom
    bottom=[i+j+k+l for i,j,k,l in zip(rs['HLA-DR1'],rs['HLA-DR2'], rs['HLA-DR3'], rs['HLA-DR4'])],
        # ],
        # with the label Planktothrix phage
    label='HLA-DR5',
        # with alpha 0.5
    alpha=0.75,
        # with color
    color='#9370DB')

# Create a bar plot, in position bar_1
ax1.bar(bar_l,
        # using the Staphylococcus phage
    rs['HLA-DR7'],
        # set the width
    width=bar_width,
        # with Pseudomonas phage and Bacillus phage and Rhodococcus phage and Propionibacterium phage and Planktothrix phage on the bottom
    bottom=[i+j+k+l+m for i,j,k,l,m in zip(rs['HLA-DR1'],rs['HLA-DR2'], rs['HLA-DR3'], rs['HLA-DR4'], rs['HLA-DR5'])],
        # with the label Staphylococcus phage
        label='HLA-DR7',
        # with alpha 0.5
        alpha=0.75,
        # with color
        color='#8B4513')


# Set the label and legends
ax1.set_ylabel("Percent of Total Dataset")
ax1.set_xlabel("Countries")
plt.legend(bbox_to_anchor=(1.18,1.02), loc='upper right', ncol=1)
plt.xticks(bar_l,B,fontweight='bold')
plt.title('HLA molecules of Individuals Affected By Rheumatic Fever')
# Set a buffer around the edge
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
