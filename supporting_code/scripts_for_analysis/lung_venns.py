'''
2021-11-20
Make ferret lung venn diagrams for index and direct animals. 
Largely adapted from mouse venn script.
KA
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import venn
from venn import venn

yellows=["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347"]
#blues=['#1844bc','#c9d5f8', '#102e7e','#5d82ea','#133490','#edf1fd']
blues=['#000000',"#013a63","#2c7da0","#61a5c2","#a9d6e5"]

       
df_UL= pd.read_csv('ferret_3664_lobe_UL_HA_rep1_barcode_clusters.csv')
df_LL= pd.read_csv('ferret_3664_lobe_LL_HA_rep1_barcode_clusters.csv')
df_UR= pd.read_csv('ferret_3664_lobe_UR_HA_rep1_barcode_clusters.csv')
df_MR= pd.read_csv('ferret_3664_lobe_MR_HA_rep1_barcode_clusters.csv')
df_LR= pd.read_csv('ferret_3664_lobe_LR_HA_rep1_barcode_clusters.csv')

ferret = {
    'UL':df_UL,
    'LL':df_LL,
    'UR':df_UR,
    'MR':df_MR,
    'LR':df_LR
    }

updated_dict={}
for key,df in ferret.items():
        if sum(df['read_count']) > 100000:
            updated_dict[key]=df

data_dict={}
for key,df in updated_dict.items():
    df=df['barcode_clusters'].values.tolist()
    #print(df)
    data_dict[key]=set(df)


fig, ax1 = plt.subplots()
venn(data_dict,fontsize=20, cmap=yellows)
plt.title('Ferret 64')
plt.tight_layout()
plt.savefig('ferret_64_venn.png',dpi=600)