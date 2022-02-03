'''
2021-07-23
Need to calculate Bray-Curtis dissimilarity for all ferret lung lobe pairings. 
Output values manually entered to be transformed into a numpy array.
Seaborn used to generate graph with partial redundancy.
KA
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
'''
df = pd.read_csv('36_lung_all.csv', skiprows=1)
new_df = df[['barcode_clusters','LR count','UR count']] #Change headers as needed to determine values for all pairings

minvalue_series = new_df.min(axis = 1)

counter=0
for item in minvalue_series:
    counter = counter + item

CIJ = counter
print('CIJ = '+str(CIJ))

SI = df['LR count'].sum()
print('SI = '+str(SI))
SJ = df['UR count'].sum()
print('SJ = '+str(SJ))

BCIJ = 1 - 2*CIJ/(SI+SJ)
print(BCIJ)
'''
#copy data into lists by hand
lobes = ['UL','LL','UR','MR','LR']
list_34 = np.array([[0,	0.914069855	,0.977626164,	0.940695726,	0.957397787],
           [0.914069855	,0,	0.988078233,	0.98858082,	0.988249833],
            [0.977626164	,0.988078233,	0,	0.967872301,	0.959049209],
            [0.940695726	,0.98858082	,0.967872301	,0,	0.705419367],
            [0.957397787	,0.988249833,	0.959049209	,0.705419367,	0]
            ])

list_36 =np.array([[0	,0.894030431	,0.995976234	,0.996065345,	0.995506274],
                    [0.894030431	,0	,0.653977213	,0.496212035	,0.637543026],
                    [0.995976234	,0.653977213,	0	,0.514307016,	0.0680123],
                    [0.996065345	,0.496212035	,0.514307016,	0,	0.481099391],
                    [0.995506274	,0.637543026,	0.0680123	,0.481099391,	0]
                        ])

#mask = np.zeros_like(list_34)
#mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    ax = sns.heatmap(list_34,cmap='YlGnBu',square=True, linewidth=0.5, vmin=0,vmax=1).set(title='Ferret 34')
    plt.savefig('34_dissimilarity.png', dpi=600)
    plt.show()
