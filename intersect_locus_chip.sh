#! /bin/bash
#SBATCH -N 1
#SBATCH -n 1

source activate microc

bedtools intersect -a ppm1g_locus.bed -b mm39_GSM2418860_WT_CTCF.bed > ctcf_locus_only.bed
