"""
2021-04-21
Make stacked area plots for HA barcodes only, for both Pst and Nhe libraries (2019 skewed versions)
Make the plots more vertical this time
"""

import time
import datetime
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.size'] = 12 #change the font size
mpl.rc('font', family='sans-serif') 
mpl.rc('font', serif='Myriad Pro') #change font to Myriad Pro, like the rest of the Illustrator figures
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

print('Start Time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

'''
#test files so i know the code works as intended
Nhe_p0 = pd.read_csv('test1.csv')
Nhe_p0_shift = pd.read_csv('test1.csv')
Nhe_p1 = pd.read_csv('test2.csv')
Nhe_p1_shift = pd.read_csv('test2.csv')
Pst_p0 = pd.read_csv('test3.csv')
Pst_p1 = pd.read_csv('test4.csv')
Pst_p0_shift=pd.read_csv('test3.csv')
Pst_p1_shift=pd.read_csv('test4.csv')

c2=['#03071e','#370617','#6a040f','#9d0208','#d00000','#dc2f02','#e85d04','#f48c06','#faa307','#ffba08']
c3=['#ffd900','#ffdd1c','#ffe139','#ffe655','#ffea71','#ffee8e','#fff2aa','#fff7c6','#fff9d1']
c4=['#081c15','#1b4332','#2d6a4f','#40916c','#52b788','#74c69d','#95d5b2','#b7e4c7','#d8f3dc']
c5=['#012a4a','#013a63','#01497c','#014f86','#2a6f97','#2c7da0','#468faf','#61a5c2','#89c2d9']
c6=['#10002b','#240046','#3c096c','#5a189a','#7b2cbf','#9d4edd','#c77dff','#e0aaff','#e6bbff']
color_list = [c2,c3,c4,c5,c6]
palette=[]
for sublist in color_list:
    for item in sublist:
        palette.append(item)
'''

c2=['#d00000','#dc2f02','#e85d04','#f48c06','#faa307','#ffba08']
c3=['#ffe655','#ffea71','#ffee8e','#fff2aa','#fff7c6','#fff9d1']
c4=['#40916c','#52b788','#74c69d','#95d5b2','#b7e4c7','#d8f3dc']
c5=['#014f86','#2a6f97','#2c7da0','#468faf','#61a5c2','#89c2d9']
c6=['#5a189a','#7b2cbf','#9d4edd','#c77dff','#e0aaff','#e6bbff']
color_list = [c2,c3,c4,c5,c6]
palette=[]
for sublist in color_list:
    for item in sublist:
        palette.append(item)


#identify file sources for each stage of library production
Nhe_p0 = pd.read_csv('Nhe_19rescue_HA_barcode_clusters.csv')
Nhe_p1 = pd.read_csv('Nhe_19amplified_HA_rep1_barcode_clusters.csv')
Pst_p0 = pd.read_csv('Pst_19rescue_HA_barcode_clusters.csv')
Pst_p1 = pd.read_csv('Pst_19amplified_HA_rep1_barcode_clusters.csv')
Nhe_p0_shift = pd.read_csv('Nhe_19rescue_HA_barcode_clusters.csv')
Nhe_p1_shift = pd.read_csv('Nhe_19amplified_HA_rep1_barcode_clusters.csv')
Pst_p0_shift = pd.read_csv('Pst_19rescue_HA_barcode_clusters.csv')
Pst_p1_shift = pd.read_csv('Pst_19amplified_HA_rep1_barcode_clusters.csv')

##############################################################################
##############################################################################
##############################################################################

#write library stage to new column in csv
Nhe_p0['Virus Passage #'] = 0
Nhe_p0_shift['Virus Passage #']=0.4
Nhe_p1['Virus Passage #'] = 1
Nhe_p1_shift['Virus Passage #']=0.6

Pst_p0['Virus Passage #'] = 0
Pst_p1['Virus Passage #'] = 1
Pst_p0_shift['Virus Passage #']=0.4
Pst_p1_shift['Virus Passage #']=0.6

#throw these dataframes into a single list per library, and a master list
Nhe_list = [Nhe_p0, Nhe_p0_shift, Nhe_p1, Nhe_p1_shift]
Pst_list = [Pst_p0, Pst_p0_shift, Pst_p1, Pst_p1_shift]
ALL_list = [Nhe_p0, Nhe_p0_shift, Nhe_p1, Nhe_p1_shift, Pst_p0, Pst_p0_shift, Pst_p1, Pst_p1_shift]

#adjust frequencies to total read count per dataframe
for df in ALL_list:
    total_reads = np.sum(df['read_count'])
    new_freq= 100.0*(df['read_count']/total_reads)
    df['new_freq'] = new_freq
    print(total_reads)

#concatenate files into one csv per library
Nhe_concat = pd.concat(Nhe_list)
Nhe_concat.to_csv(r'Nhe_HA19_barcodes_concat.csv')
Pst_concat = pd.concat(Pst_list)
Pst_concat.to_csv(r'Pst_HA19_barcodes_concat.csv')

#pivot each of the tables for ease of plotting
pivot_Nhe = Nhe_concat.pivot(index='Virus Passage #', columns='barcode_clusters', values='new_freq')
pivot_Pst = Pst_concat.pivot(index='Virus Passage #', columns='barcode_clusters', values='new_freq')

labels=[0,1]

##############################################################################
##############################################################################
##############################################################################

#Plot Nhe
print('Nhe plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax1=pivot_Nhe.plot.area(stacked=True, legend=None, color=palette, figsize=(4,12),title='HA-NheI barcodes')
ax1.tick_params(bottom=False)
plt.xticks(labels)
plt.margins(0,0)
ax1.set_ylim([0,100])
ax1.set_ylabel('frequency (%)')
plt.tight_layout()
plt.savefig('NheHA_p0_to_p1_stacked_2019_v3_TEST.png', dpi=600)
#plt.savefig('NheHA_p0_to_p1_stacked_2019_TEST.svg', dpi=600)
plt.show()
print('Nhe plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

##############################################################################
##############################################################################
##############################################################################

#Plot Pst
print('Pst plot start time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)

ax2=pivot_Pst.plot.area(stacked=True, legend=None, color=palette, figsize=(4,12),title='HA-PstI barcodes')
ax2.tick_params(bottom=False)
plt.xticks(labels)
plt.margins(0,0)
ax2.set_ylim([0,100])
ax2.set_ylabel('frequency (%)')
plt.tight_layout()
plt.savefig('PstHA_p0_to_p1_stacked_2019_v2_TEST.png', dpi=600)
#plt.savefig('PstHA_p0_to_p1_stacked_2019.svg', dpi=600)
#plt.show()
print('Pst plot end time')
readtime = datetime.datetime.fromtimestamp(time.time()).isoformat()
print(readtime)
print('DONE')
