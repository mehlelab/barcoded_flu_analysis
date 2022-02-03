'''
2021-05-24
Count singletons in lung lobes, HA only
KA
'''

import pandas as pd
import numpy as np
import math

#Ferret 34
UL_34 = pd.read_csv('HA_34_UL_barcode_clusters.csv')
LL_34 = pd.read_csv('HA_34_LL_barcode_clusters.csv')
UR_34 = pd.read_csv('HA_34_UR_barcode_clusters.csv')
MR_34 = pd.read_csv('HA_34_MR_barcode_clusters.csv')
LR_34 = pd.read_csv('HA_34_LR_barcode_clusters.csv')

#Ferret 35
MR_35 = pd.read_csv('HA_35_MR_barcode_clusters.csv')

#Ferret 36
UL_36 = pd.read_csv('36_UL_HA_barcode_clusters.csv')
LL_36 = pd.read_csv('36_LL_HA_barcode_clusters.csv')
UR_36 = pd.read_csv('36_UR_HA_barcode_clusters.csv')
MR_36 = pd.read_csv('HA_36_MR_barcode_clusters.csv')
LR_36 = pd.read_csv('36_LR_HA_barcode_clusters.csv')

lobe_list = [UL_34, LL_34, UR_34, MR_34, LR_34,
             MR_35,
             UL_36, LL_36, UR_36, MR_36, LR_36] #End up getting numbered 1-11 in order

ID = 1
for lobe in lobe_list:
    single_count=0
    print('Lobe '+str(ID))
    print('Read Count = '+str(sum(lobe['read_count'])))
    print('Total barcodes = '+str(len(lobe)))
    count_list=[]
    for item in lobe['read_count']:
        count_list.append(item)
    for item in count_list:
        if item == 1:
            single_count = single_count + 1
    print('Singletons = '+str(single_count))
    print('')
    ID = ID + 1