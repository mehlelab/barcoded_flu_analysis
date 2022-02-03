import pandas as pd
import numpy as np
import math

lungs_34 = pd.read_csv('34_lung_all.csv',skiprows=1)
lungs_36 = pd.read_csv('36_lung_all.csv',skiprows=1)
lung_list =[lungs_34,lungs_36]

for ferret in lung_list:
    single_count=0
    print('Total barcodes = '+str(len(ferret)))
    count_list=[]
    ferret['SUM']=(ferret['LL count']+ferret['UR count']+ferret['UL count']+ferret['MR count']+ferret['LR count'])
    for item in ferret['SUM']:
        count_list.append(item)
    for item in count_list:
        if item == 1:
            single_count = single_count + 1
    print('Singletons = '+str(single_count))
    print('')
