'''
2021-06-01
Make any venn I could possibly want for Ferret 34
KA, adapted heavily from Luis Haddock
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn

#load dataframes
UL = pd.read_csv('HA_34_UL_barcode_clusters.csv')
LL = pd.read_csv('HA_34_LL_barcode_clusters.csv')
UR = pd.read_csv('HA_34_UR_barcode_clusters.csv')
MR = pd.read_csv('HA_34_MR_barcode_clusters.csv')
LR = pd.read_csv('HA_34_LR_barcode_clusters.csv')
snot1 = pd.read_csv('34_1dpi_rep1_barcode_clusters.csv')
snot3 = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
snot5 = pd.read_csv('34_5dpi_rep1_barcode_clusters.csv')
trachea = pd.read_csv('34_trachea_HA_barcode_clusters.csv')
NheI_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

#convert dataframe to list format
UL_bc = UL['barcode_clusters'].values.tolist()
LL_bc = LL['barcode_clusters'].values.tolist()
UR_bc = UR['barcode_clusters'].values.tolist()
MR_bc = MR['barcode_clusters'].values.tolist()
LR_bc = LR['barcode_clusters'].values.tolist()
snot1_bc = snot1['barcode_clusters'].values.tolist()
snot3_bc = snot3['barcode_clusters'].values.tolist()
snot5_bc = snot5['barcode_clusters'].values.tolist()
trachea_bc = trachea['barcode_clusters'].values.tolist()
stock_bc = NheI_stock['barcode_clusters'].values.tolist()

whole_lung = pd.concat([UL,LL,UR,MR,LR]).drop_duplicates()
whole_lung_bc = whole_lung['barcode_clusters'].values.tolist()

all_nasal = pd.concat([snot1,snot3,snot5]).drop_duplicates()
all_nasal_bc = all_nasal['barcode_clusters'].values.tolist()

######################################################################################################
#Plot nasal washes
data_dict = {'1 dpi':set(snot1_bc), '3 dpi':set(snot3_bc),'5 dpi':set(snot5_bc)}
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_nasal_venn.png',dpi=600)
######################################################################################################
#Plot nasal washes plus trachea
data_dict = {'1 dpi':set(snot1_bc), '3 dpi':set(snot3_bc),'5 dpi':set(snot5_bc),'trachea':set(trachea_bc)}
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_nasal_trachea_venn.png',dpi=600)
######################################################################################################
#Plot trachea against whole lung
data_dict = {'trachea':set(trachea_bc),'whole lung':set(whole_lung_bc)}
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_trachea_wholeLung_venn.png',dpi=600)
######################################################################################################
#Plot 5 lung lobes
data_dict = {
    'UL':set(UL_bc),
    'LL':set(LL_bc),
    'UR':set(UR_bc),
    'MR':set(MR_bc),
    'LR':set(LR_bc)
    }
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_lung_venn.png',dpi=600)
######################################################################################################
#Plot trachea against whole lung
data_dict = {'all nasal washes':set(all_nasal_bc),'whole lung':set(whole_lung_bc)}
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_allNasal_wholeLung_venn.png',dpi=600)
######################################################################################################
#Plot stock, all nw, all lung
data_dict = {'all nasal washes':set(all_nasal_bc),'whole lung':set(whole_lung_bc),'stock':set(stock_bc)}
fig, ax1 = plt.subplots()
venn(data_dict, ax=ax1,fontsize=6)
plt.savefig('F34_stock_nw_lung_venn.png',dpi=600)
print('DONE')