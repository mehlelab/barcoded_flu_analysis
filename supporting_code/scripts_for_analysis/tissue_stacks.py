'''
2021-06-09
Try to make stackplots across tissue samples.
Lung lobe is different per graph.
Use ferret 34 to test code.
KA
'''

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
Nhe_colors = ['#102e7e','#5d82ea','#1844bc','#0e276c','#edf1fd','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe color palette

#establish source files
snot_3 = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
trachea = pd.read_csv('34_trachea_HA_barcode_clusters.csv')
lobe = pd.read_csv('HA_34_LR_barcode_clusters.csv')

#establish shifted files to make graphs flat
snot_3_shift = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
trachea_shift = pd.read_csv('34_trachea_HA_barcode_clusters.csv')
lobe_shift = pd.read_csv('HA_34_LR_barcode_clusters.csv')

#attach x axis points in each dataframe
snot_3['x_axis']=0.5
trachea['x_axis']=2.5
lobe['x_axis']=4.5
snot_3_shift['x_axis']=1.5
trachea_shift['x_axis']=3.5
lobe_shift['x_axis']=5.5

animal_list = [snot_3, snot_3_shift, trachea, trachea_shift, lobe, lobe_shift]

# Make sure all the freqs are calculated correctly
for df in animal_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)
    
#concatenate all dataframes for this single animal, then pivot
animal_concat = pd.concat(animal_list)
concat_pivot = animal_concat.pivot_table(index='x_axis',columns='barcode_clusters', values='new_freq')

print('plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

graph=concat_pivot.plot.area(stacked=True, legend=None, color=Nhe_colors, 
                           title='F34, 3dpi snot > trachea > LR')
graph.set_xlabel('tissue')

graph.set_ylabel('frequency (%)')
plt.margins(0,0)
plt.savefig('34_nw3_tr_LR_stacked.png',dpi=600)

print('plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)