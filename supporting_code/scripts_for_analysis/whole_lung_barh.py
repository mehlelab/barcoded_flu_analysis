'''
2021-06-10
How do our ferret WHOLE lungs compare to stocks?
Just plot the 3 whole lung compositions here, compare to the stock from a different script run (since 
        stock takes forever to run).
Adapted from my trachea bar_h script.
KA
'''

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

whole_34 = pd.read_csv('34_lung_all.csv',skiprows=1)
whole_35 = pd.read_csv('HA_35_MR_barcode_clusters.csv')
whole_36 = pd.read_csv('36_lung_all.csv',skiprows=1)

whole_dict = {'34':whole_34,
              '35':whole_35,
              '36':whole_36}

for key,df in whole_dict.items():
    print(key)
    print('# unique bc ',((len(df))-1))
    df['animal'] = str(key)
    total_reads = np.sum(df['read_count'])
    new_freq=100.0*df['read_count']/total_reads
    df['new_freq']=new_freq

df_concat = pd.concat(whole_dict) #get all lobes for a single animal into one CSV file
df_pivot=df_concat.pivot_table(index='animal', columns='read_id', values='new_freq')

ax=df_pivot.plot.barh(stacked=True, legend=False,color=HA_colors, title='Whole lung HA barcode frequency')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('whole_lung.png',dpi=600)

print('Graph End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

plt.show()