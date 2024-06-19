import numpy as np
import sys
import os

"""
Maps pairs to ctcf sites for making a contact map
"""

slice_one = sys.argv[1]
slice_two = sys.argv[2]
last = sys.argv[3]

pairs = []
raw_pairs = []
with open("RCMC_WT_mm39.merged.unique.pairs") as f:
    for line in f:
        current = line.strip('\n').split('\t')
        # filter out any pairs that are more than chromatin_len bp apart
        # because we only want pairs from our ROI
        try:
            if current[1][0:3] == 'chr': 
                raw_pairs.append(line)
                pairs.append([])
                pairs[-1].append([current[1], current[5], int(current[2])])
                pairs[-1].append([current[3], current[6], int(current[4])])
                pairs[-1].append(current[7])
        except:
            continue
if last==False:
    pairs = pairs[slice_one:slice_two]
    raw_pairs = pairs[slice_one:slice_two]
elif last==True:
    pairs = pairs[slice_one:]
    raw_pairs = pairs[slice_one:]
print('Pairs loaded...')
to_write = [[] for i in range(4)]
for pair_ind, pair in enumerate(pairs):
    strand_one = pairs[pair_ind][0][1]
    strand_two = pairs[pair_ind][1][1]
    """ INWARD """
    if strand_one == '+' and strand_two == '-':
        to_write[0].append(raw_pairs[pair_ind])
    """ OUTWARD """
    if strand_one == '-' and strand_two == '+':
        to_write[1].append(raw_pairs[pair_ind])
    """ TANDEM ENTRY """
    if strand_one == '+' and strand_two == '+':
        to_write[2].append(raw_pairs[pair_ind])
    """ TANDEM EXIT """
    if strand_one == '-' and strand_two == '-':
        to_write[3].append(raw_pairs[pair_ind])
fns = ['RCMC_in'+slice_one+'.pairs', \
        'RCMC_out'+slice_one+'.pairs', \
        'RCMC_tentry'+slice_one+'.pairs',\
        'RCMC_texit'+slice_one+'.pairs']
for ind,lines in enumerate(to_write):
    with open(fns[ind], 'w+') as f:
        f.writelines(lines)
