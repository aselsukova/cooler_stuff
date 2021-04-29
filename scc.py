import cooler
import numpy as np
import sys
import cooltools
import scipy
import pandas as pd

# correlation.py hic2.cool[1] hic.cool[2] chr[3] start[4] end [5]
# start = sys.argv[4]
# end = sys.argv[5]
# chr = sys.argv[3]

def make_sparse_df(mtx, index):
    index = str(index)
    a = mtx.to_numpy().tolist()
    b = []
    for i in range(len(a)):
        for j in range(i, len(a)): b.append((i, j, a[i][j]))
    df = pd.DataFrame(data=b, columns=['bin1','bin2','value'+index])
    df.bin1 +=1
    df.bin1 *= 5000
    df.bin2 += 1
    df.bin2 *= 5000
    return df
def make_two_sparse_matrix(mtx1,mtx2):
    df1 = make_sparse_df(mtx1,'1')
    df2 = make_sparse_df(mtx2,'2')
    return df1.merge(df2, on=['bin1','bin2'])

mtx_hic2_norm = cooler.Cooler(sys.argv[1]).matrix(balance=True, as_pixels=True)[:]
mtx_hic_norm = (cooler.Cooler(sys.argv[2]).matrix(balance=True, as_pixels=True))[:]
print(mtx_hic_norm)
print(mtx_hic2_norm)
#mtx_hic2_raw = cooler.Cooler(sys.argv[1]).matrix(balance=False, as_pixels=True)[:]
#mtx_hic_raw = (cooler.Cooler(sys.argv[2]).matrix(balance=False, as_pixels=True))[:]
result = make_two_sparse_matrix(mtx_hic2_norm,mtx_hic_norm)
new_columns = ['contact_st','contact_en','contact_count','0']
result.columns = new_columns
result.to_csv('norm_norm_coo.txt',sep=' ',index=False)

pearson = np.corrcoef(result['contact_count'],result['0'])
print(pearson)

#result = make_two_sparse_matrix(mtx_hic2_raw,mtx_hic_norm)
#new_columns = ['contact_st','contact_en','contact_count','0']
#result.columns = new_columns
#result.to_csv('norm_raw_coo.txt',sep=' ',index=False)
#pearson = np.corrcoef(result['contact_count'],result['0'])
#print(pearson)
