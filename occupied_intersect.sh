#! /bin/bash
#SBATCH -N 1
#SBATCH -n 1

source activate microc

bedtools intersect -wa -a granges_mm39.bed -b ctcf_locus_only.bed > ctcf_occupied_intersected_locus_only.bed
