# -*- coding: utf-8 -*-
"""
2021-05-03
Make stacked bar graphs for ferret lungs (34, 35, 36)
With stocks
Based heavily on the mouse code that i wrote 4/16/2021
DONT FORGET TO RENAME READ_ID COLUMN IN INPUTS BEFORE STARTING
KA
"""

import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

print('Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

#universally remove top and right spines
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

mpl.rcParams['font.size'] = 12 #change the font size
plt.rcParams['figure.figsize'] = [12, 6] #set default figure size

HA_colors = ['#102e7e','#5d82ea','#0e276c','#edf1fd','#1844bc','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #1844bc derived 10-color palette

######################################################################################################
######################################################################################################
######################################################################################################

#Ferret 34, 5 lobes plus stock, HA only

UL_34 = pd.read_csv('HA_34_UL_barcode_clusters.csv')
LL_34 = pd.read_csv('HA_34_LL_barcode_clusters.csv')
UR_34 = pd.read_csv('HA_34_UR_barcode_clusters.csv')
MR_34 = pd.read_csv('HA_34_MR_barcode_clusters.csv')
LR_34 = pd.read_csv('HA_34_LR_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_34_dict = {'UL':UL_34,
           'LL':LL_34,
           'UR':UR_34,
           'MR':MR_34,
           'LR':LR_34,
           #'Stock':Nhe_stock
           }

for key,df in ferret_34_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_34_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_34_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=HA_colors, title='F34 HA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('F34_all_lobes_rep1_barh.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()

######################################################################################################
######################################################################################################
######################################################################################################

#Ferret 35, 1 lobe only, HA only
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

MR_35 = pd.read_csv('HA_35_MR_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_35_dict = {'MR':MR_35}

for key,df in ferret_35_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_35_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_35_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=HA_colors, 
                      title='F35 HA barcode frequency (rep 1)', width=0.5, linewidth=2)
ax.set_xlabel("Frequency (%)")
ax.set_xlim(0,100.01)
plt.tight_layout()
plt.savefig('F35_HA_all_lobes_rep1_barh_TEST.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()

######################################################################################################
######################################################################################################
######################################################################################################


#Ferret 36, 5 lobes, note slight differences in file nomenclature

UL_36 = pd.read_csv('36_UL_HA_barcode_clusters.csv')
LL_36 = pd.read_csv('36_LL_HA_barcode_clusters.csv')
UR_36 = pd.read_csv('36_UR_HA_barcode_clusters.csv')
MR_36 = pd.read_csv('HA_36_MR_barcode_clusters.csv')
LR_36 = pd.read_csv('36_LR_HA_barcode_clusters.csv')
#Nhe_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

ferret_36_dict = {'UL':UL_36,
           'LL':LL_36,
           'UR':UR_36,
           'MR':MR_36,
           'LR':LR_36,
           #'Stock':Nhe_stock
           }

for key,df in ferret_36_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['Lobe ID'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq
    print('total reads ',total_reads)
    print('top bc ', df.iloc[[0]])
    

df_concat = pd.concat(ferret_36_dict) #get all lobes for a single animal into one CSV file
df_concat.to_csv('ferret_36_lobe_concat.csv')
df_pivot=df_concat.pivot_table(index='Lobe ID', columns='read_id', values='new_freq')

print('Graph Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax=df_pivot.plot.barh(stacked=True, legend=False,color=HA_colors, title='F36 HA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('F36_all_lobes_rep1_barh.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()
