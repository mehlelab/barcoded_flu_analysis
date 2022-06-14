# Barcoded Flu Analysis
---------------------------------------------------------------

## [Influenza A virus undergoes compartmentalized replication in vivo dominated by stochastic bottlenecks](https://rdcu.be/cPDuv).
Amato KA, Haddock LA, Braun KM, Meliopoulos V, Livingston B, Honce R, Schaack GA, Boehm E, Higgins CA, Barry GL, Koelle K, Schultz-Cherry S, Friedrich TC, Mehle A. 

---------------------------------------------------------------


This repository stores the scripts used to obtain and analyze [barcode](https://github.com/haddocksoto/barcoded_flu_analysis/tree/main/amplicon_sequencing) and [whole genome sequences](https://github.com/haddocksoto/barcoded_flu_analysis/tree/main/whole_genome_sequencing) from our barcoded **Influenza A Virus** study. 

The generation of barcodes and barcode frequencies from paired end fastq files (Illumina) were obtained using the following packages:
- Merged ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Mapped ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Trimmed ([BBTools](https://jgi.doe.gov/data-and-tools/bbtools/))
- Aligned and Sorted ([Samtools](https://www.htslib.org))
- Barcode extraction (Command Line toools)
- Barcode Clustering ([UMITools](https://umi-tools.readthedocs.io/en/latest/index.html))

To cite this work, please use:

*Amato KA, Haddock LA, Braun KM, Meliopoulos V, Livingston B, Honce R, Schaack GA, Boehm E, Higgins CA, Barry GL, Koelle K, Schultz-Cherry S, Friedrich TC, Mehle A. 2022. Influenza A virus undergoes compartmentalized replication in vivo dominated by stochastic bottlenecks. Nature Communications 13:3416.*

