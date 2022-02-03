'''
2021-11-08
Lets see if we can get shit to plot different colors based on reg mark
We cannot
KA
'''

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import os
directory = r'C:\Users\kamat\Desktop\NEUT\ALL_FULL_SEQ'

greens=["#d8f3dc","#081c15","#b7e4c7","#1b4332","#95d5b2","#2d6a4f","#74c69d","#40916c"]
black_white=["#adb5bd","#f8f9fa","#212529","#e9ecef","#6c757d","#dee2e6","#495057","#ced4da","#343a40"]

df0=pd.read_csv('Stock_5_processed_5_to_3__full_sequence_clean.csv')
df1=pd.read_csv('c_0wt_100esc_h17_l10_HA_passage1_rep1_processed_5_to_3__full_sequence_clean.csv')
df2=pd.read_csv('c_0wt_100esc_h17_l10_HA_passage2_rep1_processed_5_to_3__full_sequence_clean.csv')
df_0=pd.read_csv('Stock_5_processed_5_to_3__full_sequence_clean.csv')
df_1=pd.read_csv('c_0wt_100esc_h17_l10_HA_passage1_rep1_processed_5_to_3__full_sequence_clean.csv')
df_2=pd.read_csv('c_0wt_100esc_h17_l10_HA_passage2_rep1_processed_5_to_3__full_sequence_clean.csv')

df0['passage']=-.25
df_0['passage']=.25

df1['passage']=0.75
df_1['passage']=1.25

df2['passage']=1.75
df_2['passage']=2.25

labels=[0,1,2]

passages=[df0,df_0,df1,df_1,df2,df_2]

#concatenate all dataframes for this single animal
passage_concat = pd.concat(passages)

# Pivot concatenated table and define variable axes (?)
passage_pivot = passage_concat.pivot_table(index='passage', columns='barcode_clusters', values='frequency (%)')


graph=passage_pivot.plot.area(stacked=True, legend=None, color=black_white,
                           label=labels)
plt.margins(0,0)
plt.xticks(labels)
plt.savefig('c_0_100_nAb.png', dpi=600)
plt.show()
