import cooler
import numpy as np
import sys
import cooltools

# correlation.py hic2.cool[1] hic.cool[2] chr[3] start[4] end [5]

chr=sys.argv[3]
print(sys.argv[1])
start = sys.argv[4]
end = sys.argv[5]
mtx_hic2_norm = cooler.Cooler(sys.argv[1]).matrix(balance=True).fetch((chr,start,end))
mtx_hic_norm = cooler.Cooler(sys.argv[2]).matrix(balance=True).fetch((chr,start,end))

mtx_hic_norm = np.reshape(mtx_hic_norm, 40000)
mtx_hic2_norm = np.reshape(mtx_hic2_norm, 40000)

pearson = np.corrcoef(mtx_hic_norm,mtx_hic2_norm)
print('Pearson correlation btw norm&norm is ', pearson)

del mtx_hic2_norm
mtx_hic2_raw = cooler.Cooler(sys.argv[1]).matrix(balance=False).fetch((chr,start,end))
mtx_hic2_raw = np.reshape(mtx_hic2_raw, 40000)
print('norm matrix done')

pearson = np.corrcoef(mtx_hic_norm,mtx_hic2_raw)
print('Pearson correlation btw raw&norm is ', pearson)