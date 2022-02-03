'''
2021-05-24
Combine nasal wash timepoints.....and stuff
KA
'''

import pandas as pd
import numpy as np
import math
import csv

file1 = pd.read_csv('34_1dpi_rep1_barcode_clusters.csv')
file3 = pd.read_csv('34_3dpi_rep1_barcode_clusters.csv')
file5 = pd.read_csv('34_5dpi_rep1_barcode_clusters.csv')
'''
file1=pd.read_csv('test1.csv')
file3=pd.read_csv('test3.csv')
file5=pd.read_csv('test5.csv')
'''
file_list = [file1,file3,file5]
bc_list = [file1['barcode_clusters'],file3['barcode_clusters'],file5['barcode_clusters']]
#print(len(file1))
#print(len(file3))
#print(len(file5))

all_bc_list=[] #every barcode, every time
for file_name in bc_list:
    for barcode in file_name:
        all_bc_list.append(barcode)
#print(all_bc_list)
'''
#Count singles in each wash, separately
for nw in file_list:
    single_count=0
    print('Total barcodes = '+str(len(nw)))
    count_list=[]
    for item in nw['read_count']:
        count_list.append(item)
    for item in count_list:
        if item == 1:
            single_count = single_count + 1
    print('Singletons = '+str(single_count))
    print('')  

#Get a list of deduplicated barcodes, no info on counts
dedup_file = pd.concat(bc_list).drop_duplicates()
dedup_file.to_csv('test_dedup.csv')

dedup_df=pd.read_csv('test_dedup.csv')
dedup_df = dedup_df.drop(dedup_df.columns[0],axis=1) #drop the weird extra column i keep getting
'''
list_dedup=[] #every barcode, only once
for barcode in all_bc_list:
    if barcode not in list_dedup:
        list_dedup.append(barcode)
#print(len(list_dedup))
singles=0
for barcode in list_dedup:
    counter=0
    for item in all_bc_list:
        if item == barcode:
            counter=counter+1
    if counter == 1:
        singles=singles+1
print('total singles is')
print(singles)