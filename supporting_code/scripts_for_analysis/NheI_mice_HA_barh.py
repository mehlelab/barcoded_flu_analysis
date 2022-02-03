"""
2021-04-14
Make stacked bar plots for the six mice plus stock virus.
KA
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as mpl

#universally remove top and right spines
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

mpl.rcParams['font.size'] = 12 #change the font size
#mpl.rcParams['font.family'] = 'Myriad Pro' #hopefully change the font idk
plt.rcParams['figure.figsize'] = [12, 6] #set default figure size

#set color schemes
Nhe_colors = ['#c9d5f8','#5d82ea','#1844bc','#0e276c','#050d24'] #Nhe color palette
Pst_colors = ["#ffed85", "#ffe347", "#ffd900", "#efa536", "#f6f2ca"] #Pst color palette
PA_colors = ["#ade9ff", "#47ceff", "#00aeef", "#0096ce", "#003c52"] #PA color palette

#establish datasets to be plotted
nhe_L = pd.read_csv('HA_Nhe_L_rep1_barcode_clusters.csv')
nhe_LL = pd.read_csv('HA_Nhe_LL_rep1_barcode_clusters.csv')
nhe_LR = pd.read_csv('HA_Nhe_LR_rep1_barcode_clusters.csv')
nhe_NA = pd.read_csv('HA_Nhe_NA_rep1_barcode_clusters.csv')
nhe_R = pd.read_csv('HA_Nhe_R_rep1_barcode_clusters.csv')
nhe_RR = pd.read_csv('HA_Nhe_RR_rep1_barcode_clusters.csv')
stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

#these have to be done alphabetically, I don't know how to fix that
df_list=[nhe_L, nhe_LL, nhe_LR, nhe_NA, nhe_R, nhe_RR, stock]
df_label=['L','LL','LR','NA','R','RR','Stock']

#attach sample names to the correct data by adding new column
counter=0
for df in df_list:
    df['Sample Name']=df_label[counter]
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    #print df
    print(total_reads)
    counter=counter+1

#concatenate df because I don't know how else to get them on the same graph   
df_concat=pd.concat(df_list)
#save the concat so there's some trail of evidence for my manipulations/transformations
df_concat.to_csv('Nhe_mice_HA_rep1_concat.csv')
#PIVOT!
df_pivot = df_concat.pivot_table(index='Sample Name', columns='read_id', values='new_freq')

ax=df_pivot.plot.barh(stacked=True, 
                   legend=False, 
                   color=Nhe_colors, 
                   title=' Clustered HA barcodes (rep 1), NheI infected mice',
                   )
ax.set_xlabel("Frequency (%)")

plt.tight_layout()
plt.savefig('Nhe_mice_HA_rep1.png',dpi=300)
plt.savefig('Nhe_mice_HA_rep1.svg',dpi=300)
#plt.show()