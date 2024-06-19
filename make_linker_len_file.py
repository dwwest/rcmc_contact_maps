import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl
import glob
import re
import sys
import os

input_dir = 'test_sims/wlcsim/input/'
linker_len = 35.
num_nucs = 20
ctcf_occ = 200
lls = []
for n in range(num_nucs+1):
    if n < num_nucs/2 or n > num_nucs/2:
        lls.append(linker_len)
    if n == num_nucs/2:
        lls.append(ctcf_occ)
discs = [i/6 for i in lls]

with open(input_dir + 'ctcf_rcmc', 'w+') as f:
    for i in range(len(lls)):
        f.write(str(lls[i]) + '\t' + str(discs[i]) + '\n')

