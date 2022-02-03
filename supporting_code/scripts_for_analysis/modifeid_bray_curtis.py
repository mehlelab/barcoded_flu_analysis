import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
'''
df = pd.read_csv('ferret_65_ix63_5dpi.csv')
new_df = df[['barcode_clusters','UL','LR']] #Change headers as needed to determine values for all pairings

minvalue_series = new_df.min(axis = 1)

counter=0
for item in minvalue_series:
    counter = counter + item

CIJ = counter
#print('CIJ = '+str(CIJ))

SI = df['UL'].sum()
#print('SI = '+str(SI))
SJ = df['LR'].sum()
#print('SJ = '+str(SJ))

BCIJ = 1 - 2*CIJ/(SI+SJ)
print(BCIJ)
'''
FERRET=np.array([
[0,	0.95860031	,0.983797055
],
[0.95860031,	0,	0.629095178
],
[0.983797055,	0.629095178,	0
],
    ])

with sns.axes_style("white"):
    ax = sns.heatmap(FERRET,cmap='YlGnBu',square=True, 
                     linewidth=0.5, vmin=0,vmax=1).set(title='Ferret 65')
    plt.savefig('65_dissimilarity.png', dpi=600)
    plt.show()