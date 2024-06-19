#! /bin/bash
#SBATCH -n 1
#SBATCH -N 1

source activate wlcsim

python combine_pairs.py
