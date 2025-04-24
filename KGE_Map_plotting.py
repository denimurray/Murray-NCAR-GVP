# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:58:28 2024

@author: deni_
"""

import pandas as pd
import matplotlib as plt
import seaborn as sns
from matplotlib.patches import FancyArrowPatch
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
import webbrowser
import statsmodels.api as sm

#%%
#dat_all = pd.read_csv('Model Eval Metrics_r2_nrmse_nse_kge.csv')
dat_all = pd.read_csv('SCALED Model Eval Metrics_r2_nrmse_nse_kge.csv')

maxKGE = dat_all.groupby('Variable')['KGE'].max()
minKGE = dat_all.groupby('Variable')['KGE'].min()
meanKGE = dat_all.groupby('Variable')['KGE'].mean()

#read in ntn file and merge with site info
site_info = pd.read_csv('ntn.csv')
dat_all = pd.merge(dat_all, site_info, on = ['siteId', 'latitude', 'longitude'], how = 'left')
#dat_all = dat_all.loc[dat_all.KGE > 0,]

    
#%% Make the map except for DOC
dat = dat_all.loc[dat_all.Variable != 'WetDep_DOC_mgm2',]

for i in dat.Variable.unique():
    print(i)
    dat_sub = dat.loc[dat.Variable == i, ]
    
    #define sites for filtered data
    KGE_filtered = dat_sub.loc[dat_sub.KGE > 0.39,]
    
    color_min = 0.39
    color_max = 0.8
    
    # Create a map and add the grey points first
    fig = go.Figure()
    
    # Add grey points
    fig.add_trace(go.Scattergeo(
        lat=dat_sub['latitude'],
        lon=dat_sub['longitude'],
        mode='markers',
        marker=dict(
            color='black',  # Fill color for open circles
            line=dict(color='white'),  # Outline color
            size=15, 
            symbol='circle-open'  # Open circle symbol
        ),  # Change this to the desired color
        showlegend=False,     hoverinfo='none'
    
    ))
    
    # Add colored points
    fig.add_trace(go.Scattergeo(
        lat=KGE_filtered['latitude'],
        lon=KGE_filtered['longitude'],
        mode='markers',
        marker=dict(
            color=KGE_filtered['KGE'],
            colorscale='Spectral_r',
            opacity=1,
            size=18,
            cmin=color_min,
            cmax=color_max,
            line=dict(color='black'),
            colorbar=dict(title="KGE",  titlefont=dict(size=45), tickfont=dict(size=40))
        ),
        hoverinfo='none', showlegend=False
    ))
    
    # Update the layout of the map
    fig.update_layout(
        title=i,
        geo=dict(
            scope='usa',
            showland=True,
            showcountries=True,
            countrycolor='black',  # Outline color
            showcoastlines=True,
            coastlinecolor='black',  # Coastline color
            showlakes=True,
            lakecolor='white',
            projection_scale= 0.9,# 
            center=dict(lat=37, lon=-95),
            bgcolor='white',
            subunitcolor='black',
            subunitwidth=0.4,
            countrywidth=0.3,
            landcolor='white'  # Background color
        )
    )
    
    # Render the figure in Spyder
    fig.write_html(f'KGE_Map_{i}.html')
    
    # Open the HTML file in the default web browser
    webbrowser.open(f'KGE_Map_{i}.html')

#%% Make the DOC map:
dat_DOC = dat_all.loc[dat_all.Variable == 'WetDep_DOC_mgm2',]

doc_all = pd.read_csv('DOC_wetdep_compiled_passed cleaning.csv')
doc_all_sites = doc_all[['siteId', 'latitude', 'longitude']].drop_duplicates()


#define sites for filtered data
KGE_filtered = dat_DOC.loc[dat_DOC.KGE > 0.39,]
    
color_min = 0.39
color_max = 0.8
    
# Create a map and add the grey points first
fig = go.Figure()

# Add grey points
fig.add_trace(go.Scattergeo(
        lat=doc_all_sites['latitude'],
        lon=doc_all_sites['longitude'],
        mode='markers',
        marker=dict(
            color='black',  # Fill color for open circles
            line=dict(color='white'),  # Outline color
            size=15, 
            symbol='circle-open'  # Open circle symbol
        ),  # Change this to the desired color
        showlegend=False,     hoverinfo='none'
    
    ))
    
# Add colored points
fig.add_trace(go.Scattergeo(
        lat=KGE_filtered['latitude'],
        lon=KGE_filtered['longitude'],
        mode='markers',
        marker=dict(
            color=KGE_filtered['KGE'],
            colorscale='Spectral_r',
            opacity=1,
            size=18,
            cmin=color_min,
            cmax=color_max,
            line=dict(color='black'),
            colorbar=dict(title="KGE",  titlefont=dict(size=45), tickfont=dict(size=40))
        ),
        hoverinfo='none', showlegend=False
    ))
    
# Update the layout of the map
fig.update_layout(
        title='WetDep_DOC_mgm2',
        geo=dict(
            scope='usa',
            showland=True,
            showcountries=True,
            countrycolor='black',  # Outline color
            showcoastlines=True,
            coastlinecolor='black',  # Coastline color
            showlakes=True,
            lakecolor='white',
            projection_scale= 0.9,# 
            center=dict(lat=37, lon=-95),
            bgcolor='white',
            subunitcolor='black',
            subunitwidth=0.4,
            countrywidth=0.3,
            landcolor='white'  # Background color
        )
    )
    
# Render the figure in Spyder
fig.write_html(f'KGE_Map_DOC.html')
    
# Open the HTML file in the default web browser
webbrowser.open(f'KGE_Map_DOC.html')
