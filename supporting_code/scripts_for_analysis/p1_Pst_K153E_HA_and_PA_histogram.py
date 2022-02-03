'''
2020-04
Make histograms for the stock barcode frequencies.
KA
'''

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rc


# Set defaults and make it pretty
mpl.rcParams['font.size'] = 12 #change the font size
mpl.rc('font', **{'family' : 'sans-serif', 'sans-serif' : ['Myriad Pro']})
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False

#open files and turn them into dataframes for manipulation using pandas
HA_pst = pd.read_csv('HA_Pst_stock_rep1_barcode_clusters.csv', sep=',')
PA_pst = pd.read_csv('PA_Pst_stock_rep1_barcode_clusters.csv', sep=',')

#set bin sizes (and labels for future graph)
bins=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2]

#adjust size and remove background
fig,ax = plt.subplots(facecolor='w', figsize=(5,4))
plt.style.use('default')

#Load and specifically label HA and PA
labels=['HA','PA'] #dont fuck up the order
ax.hist([HA_pst['frequency (%)'],PA_pst['frequency (%)']],
        bins=bins, label=labels,
        log=True, color=['#ffd900','#00aeef'],
        edgecolor='black')

#add tick marks
ax.tick_params(axis = 'both', which = 'major', labelsize = 12)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 12)
ax.set_xlim(0,1.2)
ax.set_ylim(0.5,1000000)

for axis in ['bottom','left']:
  ax.spines[axis].set_linewidth(1)
  
ax.xaxis.set_tick_params(width=.5)
ax.yaxis.set_tick_params(width=.5)

# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Add title, axes labels, and legend
plt.legend(loc='upper right')
plt.xlabel('frequency bin (%)')
plt.ylabel('# barcode clusters')
plt.title('K153E-PstI barcodes, p1')

fig.tight_layout()
plt.show()

fig.savefig('p1_Pst_K153E_HA_and_PA_histogram_v2.svg')