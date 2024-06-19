#!/bin/bash
#SBATCH -n 1
#SBATCH -N 1

# ADD example command line 
source activate wlcsim

task_id=$SLURM_ARRAY_TASK_ID
task_count=$SLURM_ARRAY_TASK_COUNT

num_lines=`wc -l < RCMC_WT_mm39.merged.unique.pairs`
slice=$((num_lines/task_count*task_id))
last_id=$((task_id-1))
prev_slice=$((num_lines/task_count*last_id))
last=false
if [ "$task_id" == "$task_count" ]; then
    last=true
fi
python map_pair_inds.py $prev_slice $slice $last
