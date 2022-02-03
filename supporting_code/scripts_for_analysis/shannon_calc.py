'''
2021-11-02
Try to iterate through files to calc H and evenness
KA
'''
import pandas as pd
import math
import os
import numpy as np

directory = r'C:\Users\kamat\Desktop\Sequences\Contact transmission ferrets\lobes\csv_clusters-20211123T174223Z-001\csv_clusters\barcode_clusters' 

def ShanEven(df):
    read_count=df['read_count']
    total_reads=np.sum(df['read_count'])
    df['H_input']=(read_count/total_reads)*(np.log(read_count/total_reads)) #log base natural log
    H_input=df['H_input']
    Hprime=np.sum(H_input)
    Hprime=Hprime*(-1.0)
    Hmax=np.log(len(df))
    even=Hprime/Hmax #Pielou's evenness index
    print('Shannon = '+str(Hprime))
    print('Evenness = '+str(even))
 
for filename in os.listdir(directory):
    if filename.endswith("barcode_clusters.csv"):
      
      filename2 = pd.read_csv(filename)
      if sum(filename2['read_count']) > 100000:
          print(filename)
          ShanEven(filename2)
          print()
          #continue
      else:
          continue 
    