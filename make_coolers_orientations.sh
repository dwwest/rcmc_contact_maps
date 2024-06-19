#! /bin/bash
#SBATCH -N 1
#SBATCH -n 8

source activate microc

name=$1 #  pairs filename (assumes it's in current dir)
pairs=$name'.pairs'

cool=$name'_50.cool'
cp $pairs $cool
mcool=$name'_50.mcool'
cp $cool $mcool

echo making cool file $cool
cooler cload pairs -c1 2 -p1 3 -c2 4 -p2 5 --assembly mm39 /lustre/fs4/risc_lab/store/risc_data/downloaded/mm39/chrom.sizes:50 $pairs $cool

