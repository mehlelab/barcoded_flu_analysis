"""
2021-04-16
Plot both PA and HA stacked bars plots, for both Pst and Nhe infected mice.
Also plot respective stocks. 
KA
"""
import time
import datetime
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
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

Nhe_colors = ['#102e7e','#5d82ea','#0e276c','#edf1fd','#1844bc','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe 10-color palette
Pst_colors = ["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347", "#f6f2ca",'#fff099','#ffd966','#fff6c2'] #Pst 10-color palette
PA_colors = ["#ade9ff", "#47ceff","#003c52", "#00aeef", "#0096ce", '#c2ecff','#00547a','#70d2ff','#001c29','#008bcc'] #PA 10-color palette

###################################################
###################################################
###################################################

#Plot Nhe-HA mice

#establish datasets to be plotted
nhe_ha_L = pd.read_csv('HA_Nhe_L_rep1_barcode_clusters.csv')
nhe_ha_LL = pd.read_csv('HA_Nhe_LL_rep1_barcode_clusters.csv')
nhe_ha_LR = pd.read_csv('HA_Nhe_LR_rep1_barcode_clusters.csv')
nhe_ha_NA = pd.read_csv('HA_Nhe_NA_rep1_barcode_clusters.csv')
nhe_ha_R = pd.read_csv('HA_Nhe_R_rep1_barcode_clusters.csv')
nhe_ha_RR = pd.read_csv('HA_Nhe_RR_rep1_barcode_clusters.csv')
nhe_ha_stock = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')

Nhe_HA_df_dict={
         'Mouse 6': nhe_ha_LR,
         'Mouse 5': nhe_ha_LL,
         'Mouse 4': nhe_ha_L,
         'Mouse 3': nhe_ha_NA,
         'Mouse 2': nhe_ha_RR,
         'Mouse 1': nhe_ha_R,
         'Stock': nhe_ha_stock,
         }

Nhe_HA_dict_list = []

for key in Nhe_HA_df_dict:
    #print(key)
    df=Nhe_HA_df_dict[key]
    df['Sample Name']=str(key)
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    #print df
    #print(total_reads)
    Nhe_HA_dict_list.append(df)
    
df_concat=pd.concat(Nhe_HA_dict_list)
df_concat.to_csv('Nhe_HA_mice_ALL.csv')
df_pivot = df_concat.pivot_table(index='Sample Name', columns='read_id', values='new_freq')


ax=df_pivot.plot.barh(stacked=True, legend=False,color=Nhe_colors, title='Nhe HA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('Nhe_HA_mice_all_barh.png',dpi=500)

print('Nhe HA (1/4) is done')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

###################################################
###################################################
###################################################

#Plot Nhe-PA mice

#establish datasets to be plotted
nhe_pa_L = pd.read_csv('PA_Nhe_L_rep1_barcode_clusters.csv')
nhe_pa_LL = pd.read_csv('PA_Nhe_LL_rep1_barcode_clusters.csv')
nhe_pa_LR = pd.read_csv('PA_Nhe_LR_rep1_barcode_clusters.csv')
nhe_pa_NA = pd.read_csv('PA_Nhe_NA_rep1_barcode_clusters.csv')
nhe_pa_R = pd.read_csv('PA_Nhe_R_rep1_barcode_clusters.csv')
nhe_pa_RR = pd.read_csv('PA_Nhe_RR_rep1_barcode_clusters.csv')
nhe_pa_stock = pd.read_csv('PA_Nhe_stock_rep1_barcode_clusters.csv')

Nhe_PA_df_dict={
         'Mouse 6': nhe_pa_LR,
         'Mouse 5': nhe_pa_LL,
         'Mouse 4': nhe_pa_L,
         'Mouse 3': nhe_pa_NA,
         'Mouse 2': nhe_pa_RR,
         'Mouse 1': nhe_pa_R,
         'Stock': nhe_pa_stock,
         }

Nhe_PA_dict_list = []

for key in Nhe_PA_df_dict:
    #print(key)
    df=Nhe_PA_df_dict[key]
    df['Sample Name']=str(key)
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    #print df
    #print(total_reads)
    Nhe_PA_dict_list.append(df)
    
df_concat=pd.concat(Nhe_PA_dict_list)
df_concat.to_csv('Nhe_PA_mice_ALL.csv')
df_pivot = df_concat.pivot_table(index='Sample Name', columns='read_id', values='new_freq')


ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='Nhe PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('Nhe_PA_mice_all_barh.png',dpi=500)

print('Nhe PA (2/4) is done')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

###################################################
###################################################
###################################################

#Plot Pst-HA mice

#establish datasets to be plotted
pst_ha_L = pd.read_csv('HA_Pst_L_rep1_barcode_clusters.csv')
pst_ha_LL = pd.read_csv('HA_Pst_LL_rep1_barcode_clusters.csv')
pst_ha_LR = pd.read_csv('HA_Pst_LR_rep1_barcode_clusters.csv')
pst_ha_NA = pd.read_csv('HA_Pst_NA_rep1_barcode_clusters.csv')
pst_ha_R = pd.read_csv('HA_Pst_R_rep1_barcode_clusters.csv')
pst_ha_RR = pd.read_csv('HA_Pst_RR_rep1_barcode_clusters.csv')
pst_ha_stock = pd.read_csv('HA_Pst_stock_rep1_barcode_clusters.csv')

Pst_HA_df_dict={
         'Mouse 12': pst_ha_LR,
         'Mouse 11': pst_ha_LL,
         'Mouse 10': pst_ha_L,
         'Mouse 9': pst_ha_NA,
         'Mouse 8': pst_ha_RR,
         'Mouse 7': pst_ha_R,
         'Stock': pst_ha_stock,
         }

Pst_HA_dict_list = []

for key in Pst_HA_df_dict:
    #print(key)
    df=Pst_HA_df_dict[key]
    df['Sample Name']=str(key)
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    #print df
    #print(total_reads)
    Pst_HA_dict_list.append(df)
    
df_concat=pd.concat(Pst_HA_dict_list)
df_concat.to_csv('Pst_HA_mice_ALL.csv')
df_pivot = df_concat.pivot_table(index='Sample Name', columns='read_id', values='new_freq')


ax=df_pivot.plot.barh(stacked=True, legend=False,color=Pst_colors, title='Pst HA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('Pst_HA_mice_all_barh.png',dpi=500)

print('Pst HA (3/4) is done')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

###################################################
###################################################
###################################################

#Plot Pst-PA mice

#establish datasets to be plotted
pst_pa_L = pd.read_csv('PA_Pst_L_rep1_barcode_clusters.csv')
pst_pa_LL = pd.read_csv('PA_Pst_LL_rep1_barcode_clusters.csv')
pst_pa_LR = pd.read_csv('PA_Pst_LR_rep1_barcode_clusters.csv')
pst_pa_NA = pd.read_csv('PA_Pst_NA_rep1_barcode_clusters.csv')
pst_pa_R = pd.read_csv('PA_Pst_R_rep1_barcode_clusters.csv')
pst_pa_RR = pd.read_csv('PA_Pst_RR_rep1_barcode_clusters.csv')
pst_pa_stock = pd.read_csv('PA_Pst_stock_rep1_barcode_clusters.csv')

Pst_PA_df_dict={
         'Mouse 12': pst_pa_LR,
         'Mouse 11': pst_pa_LL,
         'Mouse 10': pst_pa_L,
         'Mouse 9': pst_pa_NA,
         'Mouse 8': pst_pa_RR,
         'Mouse 7': pst_pa_R,
         'Stock': pst_pa_stock,
         }

Pst_PA_dict_list = []

for key in Pst_PA_df_dict:
    df=Pst_PA_df_dict[key]
    df['Sample Name']=str(key)
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    Pst_PA_dict_list.append(df)
    
df_concat=pd.concat(Pst_PA_dict_list)
df_concat.to_csv('Pst_PA_mice_ALL.csv')
df_pivot = df_concat.pivot_table(index='Sample Name', columns='read_id', values='new_freq')


ax=df_pivot.plot.barh(stacked=True, legend=False,color=PA_colors, title='Pst PA barcode frequency (rep 1)')
ax.set_xlabel("Frequency (%)")
plt.tight_layout()
plt.savefig('Pst_PA_mice_all_barh.png',dpi=500)

print('Pst PA (4/4) is done')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

###################################################
###################################################
###################################################

print('Is all done!')
print('End Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)