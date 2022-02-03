'''
Try to identify the intersection between CSVs
'''
import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatchest
from pywaffle import Waffle
import csv
print('Start time')
print(datetime.datetime.fromtimestamp(time.time()).isoformat())
'''
#Load data
file1 = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')
file2 = pd.read_csv('HA_Nhe_stock_rep2_barcode_clusters.csv')
file3 = pd.read_csv('HA_Nhe_stock_rep3_barcode_clusters.csv')
file4 = pd.read_csv('HA_Nhe_stock_rep4_barcode_clusters.csv')

#Append new column with the sequencing replicate number
r1=file1['rep#']='1'
r2=file2['rep#']='2'
r3=file3['rep#']='3'
r4=file4['rep#']='4'

#put barcode and rep into one dataframe together
df1=pd.concat([file1['barcode_clusters'],file1['rep#']],axis=1)
df2=pd.concat([file2['barcode_clusters'],file2['rep#']],axis=1)
df3=pd.concat([file3['barcode_clusters'],file3['rep#']],axis=1)
df4=pd.concat([file4['barcode_clusters'],file4['rep#']],axis=1)


#concatenate all replicate runs, INCLUDING DUPLICATES
stock_rep_concat=pd.concat([file1,file2,file3,file4])
stock_rep_concat.to_csv('HA_Nhe_stockreps_concat.csv')

#turn it into a list because apparently i can only do list comp
concat_list=[]
for row in stock_rep_concat['barcode_clusters']:
    concat_list.append(row)
#print(concat_list)

#concatenate all replicate runs, REMOVING DUPLICATES
concat_dedup = pd.concat([file1['barcode_clusters'],file2['barcode_clusters'],file3['barcode_clusters'],file4['barcode_clusters']]).drop_duplicates()
concat_dedup.to_csv('HA_Nhe_stockreps_concat_DEDUP.csv')

#same
dedup_list = []
for row in concat_dedup:
    dedup_list.append(row)
#print(dedup_list)
print('Pre count time')
print(datetime.datetime.fromtimestamp(time.time()).isoformat())
#Match baracode identity to it's sum occurences across the stock replicates
test_dict={}
for item in dedup_list:
    counter=0
    for bc in concat_list:
        if bc == item:
            counter=counter+1
    #print(counter)
            test_dict[item]=counter
#print(test_dict)

pd.DataFrame.from_dict(data=test_dict, orient='index').to_csv('HA_Nhe_stockreps_OVERLAP_COUNTS.csv', header=False)
'''
counting_df=pd.read_csv('HA_Nhe_stockreps_OVERLAP_COUNTS.csv',names=["barcode_clusters", "Coverage"])
c1=0
c2=0
c3=0
c4=0
for num in counting_df['Coverage']:
    if num == 1:
        c1 = c1+1
    elif num == 2 :
        c2=c2+1
    elif num == 3:
        c3=c3+1
    elif num == 4:
        c4=c4+1
    else:
        print('YIKES')
print('Present in one: ',c1)
print('Present in two: ',c2)
print('Present in three: ',c3)
print('Present in all: ',c4)

for line in counting_df:
    counting_df['scaled']=(counting_df['Coverage'])*0.25
color_list=[]
#print(counting_df['Coverage'])
#print(counting_df['scaled'])

for item in counting_df['scaled']:
    if item == 0.25:
        color_list.append('#fde725ff') #yellow
    elif item == 0.5:
        color_list.append('#2d708eff') #blue
    elif item == 0.75:
        color_list.append('#73d055ff') #green
    elif item == 1:
        color_list.append('#440154ff') #purple
fig = plt.figure(
    FigureClass=Waffle,
    #rows=5,
    title={'label': 'NheI TEST waffle chart','loc': 'left'},
    columns=500,  # Either rows or columns could be omitted
    interval_ratio_x=0,
    interval_ratio_y=0,
    values=counting_df['scaled'], colors=color_list)
fig.savefig('NheI_test.png', dpi=600)

print('End time')
print(datetime.datetime.fromtimestamp(time.time()).isoformat())