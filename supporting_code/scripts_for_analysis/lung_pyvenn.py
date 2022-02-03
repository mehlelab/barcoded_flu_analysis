'''
PyVenn test stuff, try with lung lobes I guess
2021-06-01
KA, adapted heavily from Luis Haddock
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn

#define lung lobes
#Ferret 34, HA only
UL = pd.read_csv('HA_34_UL_barcode_clusters.csv')
LL = pd.read_csv('HA_34_LL_barcode_clusters.csv')
UR = pd.read_csv('HA_34_UR_barcode_clusters.csv')
MR = pd.read_csv('HA_34_MR_barcode_clusters.csv')
LR = pd.read_csv('HA_34_LR_barcode_clusters.csv')

#convert dataframe to list format
UL_bc = UL['barcode_clusters'].values.tolist()
LL_bc = LL['barcode_clusters'].values.tolist()
UR_bc = UR['barcode_clusters'].values.tolist()
MR_bc = MR['barcode_clusters'].values.tolist()
LR_bc = LR['barcode_clusters'].values.tolist()

data_dict = {
    'UL':set(UL_bc),
    'LL':set(LL_bc),
    'UR':set(UR_bc),
    'MR':set(MR_bc),
    'LR':set(LR_bc)
    }

fig, ax = plt.subplots()
venn(data_dict, ax=ax,fontsize=6)

ax.set_title('Ferret 34')
plt.savefig('F34_lung_venn.png',dpi=600)

######################################################################################################
######################################################################################################
######################################################################################################

#define lung lobes
#Ferret 36, HA only
UL = pd.read_csv('36_UL_HA_barcode_clusters.csv')
LL = pd.read_csv('36_LL_HA_barcode_clusters.csv')
UR = pd.read_csv('36_UR_HA_barcode_clusters.csv')
MR = pd.read_csv('HA_36_MR_barcode_clusters.csv')
LR = pd.read_csv('36_LR_HA_barcode_clusters.csv')

#convert dataframe to list format
UL_bc = UL['barcode_clusters'].values.tolist()
LL_bc = LL['barcode_clusters'].values.tolist()
UR_bc = UR['barcode_clusters'].values.tolist()
MR_bc = MR['barcode_clusters'].values.tolist()
LR_bc = LR['barcode_clusters'].values.tolist()

data_dict = {
    'UL':set(UL_bc),
    'LL':set(LL_bc),
    'UR':set(UR_bc),
    'MR':set(MR_bc),
    'LR':set(LR_bc)
    }

fig, ax = plt.subplots()
venn(data_dict, ax=ax,fontsize=6)

ax.set_title('Ferret 36')
plt.savefig('F36_lung_venn.png',dpi=600)