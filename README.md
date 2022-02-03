# Barcoded Flu Analysis
---------------------------------------------------------------

# [Influenza A virus undergoes compartmentalized replication in vivo dominated by stochastic bottlenecks](https://www.biorxiv.org/content/10.1101/2021.09.28.462198v2.supplementary-material).
Amato, K.A., Haddock, L.A., Braun, K.M., Meliopoulos, V., Livingston, B., Honce, R., Schaack, G.A., Boehm, E., Higgins, C.A., 
Barry, G.L. and Koelle, K., Schultz-Cherry, S., Friedrich, T.C., Mehle, A., 2021.  bioRxiv.

---------------------------------------------------------------


This repository stores the scripts used to obtain and analyze barcode and whole genome sequences from our barcoded **Influenza A Virus** study. 

The generation of barcodes and barcode frequencies from paired end fastq files (Illumina) were obtained using:
- Merged ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Mapped ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Trimmed ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Aligned and Sorted ([Samtools](https://www.htslib.org))
- Barcode extraction (Command Line toools)
- Barcode Clustering ([UMITools](https://umi-tools.readthedocs.io/en/latest/index.html))

