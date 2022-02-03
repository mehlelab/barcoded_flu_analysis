'''
2021-09-21
Make svg for NheI replicate sequencing
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn

#load dataframes
rep1 = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')
rep2 = pd.read_csv('HA_Nhe_stock_rep2_barcode_clusters.csv')
rep3 = pd.read_csv('HA_Nhe_stock_rep3_barcode_clusters.csv')
rep4 = pd.read_csv('HA_Nhe_stock_rep4_barcode_clusters.csv')

#convert dataframe to list format
list1 = rep1['barcode_clusters'].values.tolist()
list2 = rep2['barcode_clusters'].values.tolist()
list3 = rep3['barcode_clusters'].values.tolist()
list4 = rep4['barcode_clusters'].values.tolist()

######################################################################################################
#Plot 5 lung lobes
data_dict = {
    'rep 1':set(list1),
    'rep 2':set(list2),
    'rep 3':set(list3),
    'rep 4':set(list4)
    }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('stock_overlap_venn.svg',dpi=600)

print('DONE')