"""
2021-04-26
Plot ferret nasal washes over time. 
KA
"""

import time
import datetime
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.font_manager

# Set defaults and colors
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
Nhe_colors = ['#102e7e','#5d82ea','#1844bc','#0e276c','#edf1fd','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe color palette
PA_colors = ["#ade9ff", "#47ceff","#003c52", "#00aeef", "#0096ce", '#c2ecff','#00547a','#70d2ff','#001c29','#008bcc'] #PA 10-color palette

palette=Nhe_colors

##########################################################################################################
##########################################################################################################
##########################################################################################################

#PLOT FERRET 34

# Establish data sources
snot_1 = pd.read_csv('34_1dpi_rep1_barcode_clusters.csv')
snot_3 = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
snot_5 = pd.read_csv('34_5dpi_rep1_barcode_clusters.csv')
snot_1_shift = pd.read_csv('34_1dpi_rep1_barcode_clusters.csv')
snot_3_shift = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
snot_5_shift = pd.read_csv('34_5dpi_rep1_barcode_clusters.csv')
snot_list = [snot_1,snot_1_shift,snot_3,snot_3_shift,snot_5,snot_5_shift]

# Attach dpi identifier within each dataframe
snot_1['dpi']=0.5
snot_3['dpi']=2.5
snot_5['dpi']=4.5
snot_1_shift['dpi']=1.5
snot_3_shift['dpi']=3.5
snot_5_shift['dpi']=5.5

# Make sure all the freqs are calculated correctly
for df in snot_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)
    
#concatenate all dataframes for this single animal
snot_concat = pd.concat(snot_list)

# Pivot concatenated table and define variable axes (?)
snot_pivot = snot_concat.pivot_table(index='dpi', columns='barcode_clusters', values='new_freq')

labels=[1,3,5]

#Plot
print('plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

graph=snot_pivot.plot.area(stacked=True, legend=None, color=palette, 
                           label=labels,title='F34 Nasal Washes, HA Barcodes')
graph.set_xlabel('dpi')
plt.xticks(labels)
graph.set_ylabel('frequency (%)')
plt.margins(0,0)
#plt.savefig('F34_nasal_wash_stackbar_test_blueHA.png',dpi=600)
plt.savefig('F34_nasal_wash_stackbar_blueHA.svg')
#plt.show()

print('plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

#########################################################################################################
##########################################################################################################
##########################################################################################################

#PLOT FERRET 35

# Establish data sources
snot_1 = pd.read_csv('35_1dpi_rep1_barcode_clusters.csv')
snot_3 = pd.read_csv('35_3dpi_rep1_barcode_clusters.csv')
snot_5 = pd.read_csv('35_5dpi_rep1_barcode_clusters.csv')
snot_1_shift = pd.read_csv('35_1dpi_rep1_barcode_clusters.csv')
snot_3_shift = pd.read_csv('35_3dpi_rep1_barcode_clusters.csv')
snot_5_shift = pd.read_csv('35_5dpi_rep1_barcode_clusters.csv')
snot_list = [snot_1,snot_1_shift,snot_3,snot_3_shift,snot_5,snot_5_shift]

# Attach dpi identifier within each dataframe
snot_1['dpi']=0.5
snot_3['dpi']=2.5
snot_5['dpi']=4.5
snot_1_shift['dpi']=1.5
snot_3_shift['dpi']=3.5
snot_5_shift['dpi']=5.5

# Make sure all the freqs are calculated correctly
for df in snot_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)
    
#concatenate all dataframes for this single animal
snot_concat = pd.concat(snot_list)

# Pivot concatenated table and define variable axes (?)
snot_pivot = snot_concat.pivot_table(index='dpi', columns='barcode_clusters', values='new_freq')

labels=[1,3,5]

#Plot
print('plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

graph=snot_pivot.plot.area(stacked=True, legend=None, color=palette, 
                           label=labels,title='F35 Nasal Washes, HA Barcodes')
graph.set_xlabel('dpi')
plt.xticks(labels)
graph.set_ylabel('frequency (%)')
plt.margins(0,0)
#plt.savefig('F35_nasal_wash_stackbar_blue_HA.png',dpi=600)
plt.savefig('F35_nasal_wash_stackbar_blueHA.svg')
plt.show()

print('plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

#########################################################################################################
##########################################################################################################
##########################################################################################################

#PLOT FERRET 36

# Establish data sources
snot_1 = pd.read_csv('36_1dpi_rep1_barcode_clusters.csv')
snot_3 = pd.read_csv('36_3dpi_rep1_barcode_clusters.csv')
snot_5 = pd.read_csv('36_5dpi_rep1_barcode_clusters.csv')
snot_1_shift = pd.read_csv('36_1dpi_rep1_barcode_clusters.csv')
snot_3_shift = pd.read_csv('36_3dpi_rep1_barcode_clusters.csv')
snot_5_shift = pd.read_csv('36_5dpi_rep1_barcode_clusters.csv')
snot_list = [snot_1,snot_1_shift,snot_3,snot_3_shift,snot_5,snot_5_shift]

# Attach dpi identifier within each dataframe
snot_1['dpi']=0.5
snot_3['dpi']=2.5
snot_5['dpi']=4.5
snot_1_shift['dpi']=1.5
snot_3_shift['dpi']=3.5
snot_5_shift['dpi']=5.5

# Make sure all the freqs are calculated correctly
for df in snot_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)
    
#concatenate all dataframes for this single animal
snot_concat = pd.concat(snot_list)

# Pivot concatenated table and define variable axes (?)
snot_pivot = snot_concat.pivot_table(index='dpi', columns='barcode_clusters', values='new_freq')

labels=[1,3,5]

#Plot
print('plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

graph=snot_pivot.plot.area(stacked=True, legend=None, color=palette, 
                           label=labels,title='F36 Nasal Washes, HA Barcodes')
graph.set_xlabel('dpi')
plt.xticks(labels)
graph.set_ylabel('frequency (%)')
plt.margins(0,0)
#plt.savefig('F36_nasal_wash_stackbar_blueHA.png',dpi=600)
plt.savefig('F36_nasal_wash_stackbar_blueHA.svg')
plt.show()

print('plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

print('DONE')