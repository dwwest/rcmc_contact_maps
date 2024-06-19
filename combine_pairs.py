import numpy as np
import glob

all_orients = ['in', 'out', 'tentry', 'texit']
all_fns = ['RCMC_'+o+'.pairs' for o in all_orients]
for i in range(4):
    files = glob.glob('./RCMC_'+all_orients[i]+'*.pairs')
    with open(all_fns[i], 'a') as all_f:
        for fi in files:
            with open(fi, 'r') as f:
                lines = f.readlines()
                all_f.writelines(lines)


