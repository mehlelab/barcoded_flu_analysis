'''
2020-04
Make histograms showing binned frquencies for barcodes.
KA
'''

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Set defaults
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.top'] = False


#open files and turn them into dataframes for manipulation using pandas
HA_nhe = pd.read_csv('HA_Nhe_stock_rep1_barcode_clusters.csv', sep=',')
PA_nhe = pd.read_csv('PA_Nhe_stock_rep1_barcode_clusters.csv', sep=',')

#set bin sizes (and labels for future graph)
bins=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2]
#bin_labels = ['0-0.05%', '0.05-0.1%', '0.1-0.15%', '0.15-0.2%', '0.2-0.25%', '0.25-0.3%', '0.3-0.35%', '0.35-0.4%', '0.4-0.45%', '0.45-0.5%']

#adjust size and remove background
fig,ax = plt.subplots(facecolor='w', figsize=(5,4))
plt.style.use('default')

#Load and specifically label HA and PA
labels=['HA','PA'] #dont fuck up the order
ax.hist([HA_nhe['frequency (%)'],PA_nhe['frequency (%)']],
        bins=bins, label=labels,
        log=True, color=['mediumblue','deepskyblue'],
        edgecolor='black')

#Add title, axes labels, and legend
plt.legend(loc='upper right')
plt.xlabel('frequency bin (%)')
plt.ylabel('# barcode clusters')
plt.title('K153E-NheI barcodes, p1')

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

fig.tight_layout()
plt.show()

fig.savefig('p1_Nhe_K153E_HA_and_PA_histogram_v2.svg')