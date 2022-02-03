'''
Try to identify the intersection between CSVs
Nhe ferret 36
'''

import pandas as pd
'''
file1 = pd.read_csv('HA_34_UL_barcode_clusters.csv')
file2 = pd.read_csv('HA_34_LL_barcode_clusters.csv')
file3 = pd.read_csv('HA_34_UR_barcode_clusters.csv')
file4 = pd.read_csv('HA_34_MR_barcode_clusters.csv')
file5 = pd.read_csv('HA_34_LR_barcode_clusters.csv')
#file7=pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv')
'''
file1 = pd.read_csv('36_UL_HA_barcode_clusters.csv')
file2 = pd.read_csv('36_LL_HA_barcode_clusters.csv')
file3 = pd.read_csv('36_UR_HA_barcode_clusters.csv')
file4 = pd.read_csv('HA_36_MR_barcode_clusters.csv')
file5 = pd.read_csv('36_LR_HA_barcode_clusters.csv')

#stock=file7['barcode_clusters']
bc_1=file1['barcode_clusters']
bc_2=file2['barcode_clusters']
bc_3=file3['barcode_clusters']
bc_4=file4['barcode_clusters']
bc_5=file5['barcode_clusters']

#Convert the list into a collection,Find the intersection using the set operator,Then convert back to list type
#https://www.tutorialfor.com/blog-201390.htm
intersection=list (set (bc_1)&set (bc_2)&set (bc_3)&set (bc_4)&set (bc_5))

print(intersection)
print(len(intersection))

print('total barcodes per lobe')
lobe_list = [file1,file2,file3,file4,file5]
for lobe in lobe_list:
    print(len(lobe))

concat_dedup = pd.concat([file1['barcode_clusters'],file2['barcode_clusters'],file3['barcode_clusters'],file4['barcode_clusters']]).drop_duplicates()
#concat_dedup.to_csv('test34_DEDUP.csv')

print('# barcodes after removing duplicates')
print(len(concat_dedup))