'''
2021-10-19
Make stacked bar plots for the new index/contact ferrets 
Don't forget to appeand read_id into each of the referenced files.
KA
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#universally remove top and right spines
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['font.size'] = 16

#mpl.rcParams['font.size'] = 16 #change the font size
#plt.rcParams['figure.figsize'] = [12, 6] #set default figure size

HA_yellows=["#ffed85", "#efa536","#ffd900",'#ffe75c','#f5d000',"#ffe347", "#f6f2ca",'#fff099','#ffd966','#fff6c2']
HA_blues = ['#102e7e','#5d82ea','#1844bc','#0e276c','#edf1fd','#c9d5f8', '#050d24', '#4a74e8','#133490','#020712'] #Nhe color palette

#define input files
UL_3665 = pd.read_csv('ferret_3665_lobe_UL_HA_rep1_barcode_clusters.csv')
LL_3665 = pd.read_csv('ferret_3665_lobe_LL_HA_rep1_barcode_clusters.csv')
UR_3665 = pd.read_csv('ferret_3665_lobe_UR_HA_rep1_barcode_clusters.csv')
MR_3665 = pd.read_csv('ferret_3665_lobe_MR_HA_rep1_barcode_clusters.csv')
LR_3665 = pd.read_csv('ferret_3665_lobe_LR_HA_rep1_barcode_clusters.csv')
empty=pd.read_csv('empty.csv')

#turn input files into dictionaries, that can then be passed into the barh function
ferret_3665_dict = {'UL':UL_3665,
           'LL':LL_3665,
           'UR':UR_3665,
           'MR':MR_3665,
           'LR':LR_3665
           }

def read_threshold(ferret):
    for key,df in ferret.items():
        if sum(df['read_count']) < 100000:
            newvalue=pd.read_csv('empty.csv')
            print('remove '+key)
            #print(sum(df['read_count']))
            #print(df)
            ferret[key]=newvalue

#write function to append lung lobe id into each ferret file
def lobe_id(ferret):
    for key,df in ferret.items():
        df['Lobe ID']=str(key)
        #print(str(key))
        #print(len(df))
        #print(sum(df['read_count']))


def barh(ferret,graph_title):
	#concatenate a single ferret so that all its lobes show up on the same graph
	df_concat = pd.concat(ferret)
	df_pivot =df_concat.pivot_table(index='Lobe ID', columns='read_id',values='frequency (%)')
	#make the graph
	ax=df_pivot.plot.barh(stacked=True, legend=False, color=HA_yellows, title=str(graph_title))
	ax.set_xlabel("Frequency (%)"), plt.xlim(0,100)
	plt.tight_layout()
	plt.savefig(graph_title+'.png',dpi=600)
	plt.show()

read_threshold(ferret_3665_dict)
lobe_id(ferret_3665_dict)
barh(ferret_3665_dict, 'Ferret 65')