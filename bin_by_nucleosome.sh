#! /bin/bash
#SBATCH -N 1
#SBATCH -n 1

source activate microc

python bin_by_nucleosome.py
