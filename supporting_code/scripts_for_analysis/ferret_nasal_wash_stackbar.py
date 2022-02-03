"""
2021-09-24
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
HA_blues = ['#102e7e','#5d82ea','#1844bc','#0e276c','#edf1fd','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe color palette
#HA_blues = ['#102e7e','#5d82ea','#1a3765','#edf1fd','#0e276c','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe color palette
HA_yellows=["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347", "#f6f2ca",'#fff099','#ffd966','#fff6c2']

palette=HA_blues

##########################################################################################################
##########################################################################################################
##########################################################################################################

#PLOT FERRET 3668

# Establish data sources
snot_1 = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_3 = pd.read_csv('ferret_3668_nw_3dpi_HA_rep1_barcode_clusters.csv')
snot_5 = pd.read_csv('ferret_3668_nw_5dpi_HA_rep1_barcode_clusters.csv')
snot_1_shift = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_3_shift = pd.read_csv('ferret_3668_nw_3dpi_HA_rep1_barcode_clusters.csv')
snot_5_shift = pd.read_csv('ferret_3668_nw_5dpi_HA_rep1_barcode_clusters.csv')
'''
#establish empties as needed
#should take adjacent day's dataframe and set everything to zero for missing data
snot_5 = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_5_shift = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_5['frequency (%)']=0
snot_5_shift['frequency (%)']=0
snot_3 = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_3_shift = pd.read_csv('ferret_3668_nw_1dpi_HA_rep1_barcode_clusters.csv')
snot_3['frequency (%)']=0
snot_3_shift['frequency (%)']=0
'''
#Make list of all dataframes for plotting
snot_list = [snot_1,snot_1_shift,snot_3,snot_3_shift,snot_5,snot_5_shift]

# Attach dpi identifier within each dataframe
snot_1['dpi']=0.5
snot_3['dpi']=2.5
snot_5['dpi']=4.5
snot_1_shift['dpi']=1.5
snot_3_shift['dpi']=3.5
snot_5_shift['dpi']=5.5
'''
# Make sure all the freqs are calculated correctly
for df in snot_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)
 '''   
#concatenate all dataframes for this single animal
snot_concat = pd.concat(snot_list)

# Pivot concatenated table and define variable axes (?)
snot_pivot = snot_concat.pivot_table(index='dpi', columns='barcode_clusters', values='frequency (%)')

labels=[1,3,5]

#Plot
print('plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

graph=snot_pivot.plot.area(stacked=True, legend=None, color=palette, 
                           label=labels,title='F3668 Nasal Washes, HA Barcodes')
graph.set_xlabel('dpi')
plt.xticks(labels)
graph.set_ylabel('frequency (%)')
plt.margins(0,0)

plt.savefig('F3668_nasal_wash_stackbar_HA_v2.png', dpi=600)
plt.show()

print('plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

print('DONE')