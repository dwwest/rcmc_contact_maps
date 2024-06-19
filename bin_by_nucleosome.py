import numpy as np

for ctcf_ind in [6, 16]:

    # the nucleosome centers are determined in fig_4 code,
    # from aggregated ctcf sites -- we assume an nrl of 167 and
    # take take the three 50bp bins that best match that
    # site
    ctcf_center = int(162/2) - 1 # because of 0 index
    ctcf_occ = 100
    wrap = 127
    link = 30
    nrl = wrap + link
    chrom_length = 162*50
    num_nucs = 20
    # see make_heatmap.py in the fig_4 folder for more info on this choice
    nuc_centers = [i+chrom_length/2 for i in range(ctcf_occ+int(nrl/2), ctcf_occ+int(nrl/2)+int(nrl*(num_nucs/2)), nrl)]
    nuc_centers = nuc_centers + [-i+chrom_length/2 for i in range(ctcf_occ+int(nrl/2), ctcf_occ+int(nrl/2)+int(nrl*(num_nucs/2)), nrl)]
    nuc_centers.sort()

    bin_boundaries = [i for i in range(0,int(chrom_length),50)]

    bin_inds = []
    for n in nuc_centers:
        bin_inds.append(next(x[0] - 1 for x in enumerate(bin_boundaries) if x[1] > n))

    bins_for_nucs = np.array([[i-1,i+2] for i in bin_inds])

    matrix = np.load('adjusted_ctcf_region_%s.npy'%str(ctcf_ind))
    nuc_res_matrix = np.zeros([num_nucs**2, 4])

    # bin nucleosomes
    ind = 0
    for bin_set_a in bins_for_nucs:
        for bin_set_b in bins_for_nucs:
            for o in range(4):
                nuc_res_matrix[ind,o] = np.sum(matrix[bin_set_a[0]:bin_set_a[1],bin_set_b[0]:bin_set_b[1],o])
            ind += 1

    nuc_res_matrix = np.reshape(nuc_res_matrix,[num_nucs, num_nucs, 4])
    np.save('nuc_res_matrix_%s.npy'%str(ctcf_ind),nuc_res_matrix)

    to_save_dir = 'test_sims/wlcsim/isd_input/micro-c_data/rcmc_%s/'%str(ctcf_ind)
    with open(to_save_dir + '/data.txt', 'w+') as f:
        for i in range(num_nucs-1):
            for j in range(i+1,num_nucs):
                for k in range(1,4):
                    f.write(str(int(100000000*nuc_res_matrix[i,j,k])) + '\n') # large # mult is to get them to be pseudocounts because the simulation will expect whole numbers



