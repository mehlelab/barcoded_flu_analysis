'''
Be careful to only do stuff with 100k reads
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

#df1= pd.read_csv("ferret_3665_lobe_UR_HA_rep1_barcode_clusters.csv")
df1=pd.read_csv('ferret_3670_nw_1dpi_HA_rep1_barcode_clusters.csv')
df2=pd.read_csv('ferret_3670_nw_3dpi_HA_rep1_barcode_clusters.csv')
#df4=pd.read_csv('ferret_3669_lobe_MR_HA_rep1_barcode_clusters.csv')
#df5=pd.read_csv('ferret_3669_lobe_UL_HA_rep1_barcode_clusters.csv')
#df6=pd.read_csv('ferret_3669_nw_1dpi_HA_rep1_barcode_clusters.csv')
df_list=[df1,df2]

new_list=[]
for df in df_list:
    print(len(df))
    for barcode in df['barcode_clusters']:
        new_list.append(barcode)

list_dedup=list(set(new_list))
new_df=pd.DataFrame(list_dedup)
new_df.to_csv('ferret7013dpi.csv')

#For nasal washes, 3dpi>first postiive dpi
#except 69-71 which is 1-1dpi