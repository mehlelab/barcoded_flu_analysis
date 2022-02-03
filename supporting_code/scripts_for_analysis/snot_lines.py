"""
2021-04-25
Plot ferret nasal washes over time. Hopefully, most barcodes cluster near <1%,
and you see the couple barcodes that increase/decrease around the 10% mark.
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

# Set defaults and make it pretty
mpl.rcParams['font.size'] = 12 #change the font size
mpl.rc('font', family='sans-serif') 
mpl.rc('font', serif='Myriad Pro') #change font to Myriad Pro, like the rest of the Illustrator figures
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
Nhe_colors = ['#102e7e','#5d82ea','#0e276c','#1844bc','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe 0-color palette

# Establish data sources
snot_1 = pd.read_csv('36_1dpi_rep1_barcode_clusters.csv')
snot_3 = pd.read_csv('36_3dpi_rep1_barcode_clusters.csv')
snot_5 = pd.read_csv('36_5dpi_rep1_barcode_clusters.csv')
snot_list = [snot_1,snot_3,snot_5]

# Attach dpi identifier within each dataframe
snot_1['dpi']=1
snot_3['dpi']=3
snot_5['dpi']=5

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

# Plot that snot
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print('Start'+readtime)
graph = snot_pivot.plot(legend=False,color=Nhe_colors, title='Ferret 36 Nasal Washes')
graph.set_xlabel('dpi')
plt.xticks(np.arange(1, 5.1, 2))
graph.set_ylabel('frequency (%)')
plt.margins(0,0)

plt.savefig('F36_snot_dpi.png',dpi=500)
plt.show()

readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print('End'+readtime)