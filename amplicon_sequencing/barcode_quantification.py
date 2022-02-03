#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import glob
import csv
from pathlib import Path
from umi_tools import UMIClusterer
import numpy as np
import matplotlib.pyplot as plt
import json
import requests

#reading all txt files as a pandas dataframes an generating csv with barcodes 
#and read counts

folder='data_output/'
for file in Path(folder).glob('*/*barcodes_clean.txt'):
    df=pd.read_csv(file, header=None)
    df.columns=["barcodes"]
    df=df["barcodes"].value_counts().rename_axis('barcodes').reset_index(name='read_count')
    df.to_csv(file.with_suffix('.csv'), index = False)


#Preparing each barcode list for clustering

#We use the UMI-Tools adjacency clustering methods (doi: 10.1101/gr.209601.116; Smith, et al. 2017)


clusterer = UMIClusterer(cluster_method="adjacency")

for file in Path(folder).glob('*/*barcodes_clean.csv'):
    new_data = pd.read_csv(file, sep=',')
    new_data = new_data[['barcodes', 'read_count']]
    new_data.sort_values('read_count', ascending=False, inplace=True)
    new_data_dict = new_data.set_index('barcodes')['read_count'].to_dict()
    new_data_dict = {k.encode('utf8'): v for k, v in new_data_dict.items()}
    #applying the UMI-clusterer:
    clustered_new_data_bc = clusterer(new_data_dict, threshold=1)
    total_read_count_per_cluster_list = []
    for cluster in clustered_new_data_bc:
        clustertotal=0
        for barcode in cluster:
            clustertotal += new_data_dict[barcode]
        total_read_count_per_cluster_list.append(clustertotal)
    clustered_rcs = []
    for cluster in clustered_new_data_bc:
        tempreadlist = []
        for barcode in cluster:
            tempreadlist.append(new_data_dict[barcode])
        clustered_rcs.append(tempreadlist)
    clustered_bc_df = pd.DataFrame(clustered_new_data_bc)
    clustered_rcs_df = pd.DataFrame(clustered_rcs)
    clustered_bc_df_first = clustered_bc_df[clustered_bc_df.columns[0]]
    clustered_rcs_df_first = clustered_rcs_df[clustered_rcs_df.columns[0]]
    clusters = pd.concat([clustered_bc_df_first, clustered_rcs_df_first], axis=1)
    clusters.columns = ['barcode_clusters', 'read_count']
    num_reads = new_data['read_count'].sum()
    clusters_temp = clusters['read_count'].div(num_reads).mul(100).to_frame('frequency (%)')
    clusters_final = pd.concat([clusters, clusters_temp], axis=1)
    clusters_final['barcode_clusters'] = clusters_final['barcode_clusters'].str.decode("utf-8")
    clusters_final = clusters_final.sort_values(by=["frequency (%)"], ascending=False)
    clusters_final.to_csv(file.with_suffix('.csv'), index = False)
    
#Output will be a csv file with clustered barcodes, read counts and relative frequencies
