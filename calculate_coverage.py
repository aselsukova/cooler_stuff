import cooler
from cooltools import coverage
import sys

clr = cooler.Cooler(sys.argv[1])
print('read file')
cis, total = coverage.get_coverage(clr,  ignore_diags = 1)
print('calculate cov')
chrm_sizes_bins = clr.chromsizes.apply(lambda x : x//clr.binsize)
current_bin=0
chrm_coverage = []
for chrm in chrm_sizes_bins:
    print(chrm)
    chrm_coverage.append(coverage)
    i = 0
    coverage = 0
    while(i<=chrm):
        coverage += total[current_bin]
        i+=1
        current_bin += 1
        if(current_bin % 10000 == 0):
            print('calculate ',current_bin,' bins')
print(chrm_coverage)
