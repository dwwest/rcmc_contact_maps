#! /bin/bash
#SBATCH -N 1
#SBATCH -n 1

source activate microc

python adjust_orientations.py
