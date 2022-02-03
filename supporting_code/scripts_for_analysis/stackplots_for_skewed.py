"""
2021-04-19
Make stacked area plots for HA barcodes only, for both Pst and Nhe libraries (2019 skewed versions)
"""

import time
import datetime
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

print('Start Time')
print(readtime)

#set color scheme for plots
Nhe_colors = ['#102e7e','#5d82ea','#0e276c','#edf1fd','#1844bc','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe 10-color palette
Pst_colors = [ "#efa536","#ffed85","#ffd900",'#ffe75c','#f5d000', "#f6f2ca","#ffe347",'#fff099','#ffd966','#fff6c2'] #Pst 10-color palette

#test files so i know the code works as intended
Nhe_p0 = pd.read_csv('test1.csv')
Nhe_p1 = pd.read_csv('test2.csv')
Pst_p0 = pd.read_csv('test3.csv')
Pst_p1 = pd.read_csv('test4.csv')

'''
#identify file sources for each stage of library production
Nhe_p0 = pd.read_csv('Nhe_19rescue_HA_barcode_clusters.csv')
Nhe_p1 = pd.read_csv('Nhe_19amplified_HA_barcode_clusters.csv')
Pst_p0 = pd.read_csv('Pst_19rescue_HA_barcode_clusters.csv')
Pst_p1 = pd.read_csv('Pst_19amplified_HA_barcode_clusters.csv')
'''
#write library stage to new column in csv
Nhe_p0['Virus Passage #'] = 0
Nhe_p1['Virus Passage #'] = 1
Pst_p0['Virus Passage #'] = 0
Pst_p1['Virus Passage #'] = 1

#throw these dataframes into a single list per library, and a master list
Nhe_list = [Nhe_p0, Nhe_p1]
Pst_list = [Pst_p0, Pst_p1]
ALL_list = [Nhe_p0, Nhe_p1, Pst_p0, Pst_p1]

#adjust frequencies to total read count per dataframe
for df in ALL_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)

#concatenate files into one csv per library
Nhe_concat = pd.concat(Nhe_list)
Nhe_concat.to_csv(r'Nhe_HA_barcodes_concat.csv')
Pst_concat = pd.concat(Pst_list)
Pst_concat.to_csv(r'Pst_HA_barcodes_concat.csv')

print('Pre plot Time')
print(readtime)

#pivot each of the tables for ease of plotting
pivot_Nhe = Nhe_concat.pivot(index='Virus Passage #', columns='barcode_clusters', values='new_freq')
pivot_Pst = Pst_concat.pivot(index='Virus Passage #', columns='barcode_clusters', values='new_freq')

labels=[0,1]

#Plot Nhe
print('Nhe start time')
print(readtime)


ax1=pivot_Nhe.plot.area(stacked=True, legend=None, color=Nhe_colors)
ax1.tick_params(bottom=False)
plt.xticks(labels)
plt.margins(0,0)
ax1.set_ylim([0,100])
ax1.set_ylabel('frequency (%)')
plt.savefig('test.png',dpi=600)

print('Nhe end time')
print(readtime)

#Plot Pst
print('Pst start time')
print(readtime)

ax2=pivot_Pst.plot.area(stacked=True, legend=None, color=Pst_colors)
ax2.tick_params(bottom=False)
plt.xticks(labels)
plt.margins(0,0)
ax2.set_ylim([0,100])
ax2.set_ylabel('frequency (%)')
plt.savefig('test2.png', dpi=600)

print('Pst end time')
print(readtime)
