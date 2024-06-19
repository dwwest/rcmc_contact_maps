import numpy as np

"""
This is here to take the  file for occupied ctcf sites and extend the grange out by 2000 bp on either side
so that I can intersect for micro-c pairs that fall not directly on the 
ctcf site but on +5 and +6 nucleosomes as well
"""

bp_to_extend = 4000 # how many bp to extend out from granges
with open('ctcf_occupied_intersected_locus_only.bed', 'r') as f_og, open('ctcf_occupied_intersected_expanded_locus_only.bed', 'w+') as f_expand:
    f_expand.write('# \n')
    for ind,line in enumerate(f_og):
        current = line.strip('\n').split('\t')
        # extend range back by bp_to_extend
        if int(current[1]) - bp_to_extend >= 0:
            current[1] = str(int(current[1]) - bp_to_extend)
        # extend range forward by bp_to_extend
        current[2] = str(int(current[2]) + bp_to_extend)
        # write larger grange to granges_expanded file
        f_expand.write('\t'.join(current) + '\n')
