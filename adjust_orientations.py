import numpy as np
import cooler

ctcfs = []
with open('/ru-auth/local/home/dwest/scratch/2023_BAYES_PAPER/fig_5/ctcf_occupied_intersected_expanded_locus_only.bed', 'r') as f:
    for line in f:
        ctcfs.append(line.strip('\n').split('\t'))

site_inds = [6, 16] # chosen by inspection as two sites with significantly different map structure
for ind in site_inds:
    map_inds = ctcfs[ind]
    to_save_ind_label = str(ind)
    orientations = ['RCMC_%s_50.cool'%o for o in ['in','out','tentry','texit']] 
    region = np.zeros([162, 162,4])
    for i, orient in enumerate(orientations):
        # want to just do this for regions of interest
        # go through ctcf sites and pull out the matricies
        # want to add up the vals from all orientations for each
        # matrix and then get factor difference by dividing the main
        # cooler by that, then element-wise multiplication 
        c = cooler.Cooler(orient)
        region[:,:,i] = c.matrix(balance=False).fetch((map_inds[0], int(map_inds[1]), int(map_inds[2])))

    unbalanced = np.sum(region, axis=2)

    # get region of interest of balanced matrix
    c = cooler.Cooler('RCMC_WT_mm39.merged.50.mcool::resolutions/50')
    balanced = c.matrix().fetch((map_inds[0], int(map_inds[1]), int(map_inds[2])))

    factor = np.divide(balanced, unbalanced)
    np.save('factors_%s.npy'%to_save_ind_label, factor)

    # adjust each orientation and save
    adjusted = np.zeros([162, 162, 4])
    for i in range(4):
        adjusted[:,:,i] = np.nan_to_num(np.multiply(region[:,:,i], factor))
    np.save('adjusted_ctcf_region_%s.npy'%to_save_ind_label, adjusted)

