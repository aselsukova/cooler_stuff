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
coverage = 0
for chrm in chrm_sizes_bins:
    # print(chrm)
    if(coverage != 0):
        chrm_coverage.append(int(coverage))
    coverage = 0
    i = 0
    while(i<=chrm):
        coverage += total[current_bin]
        i+=1
        current_bin += 1
        # if(current_bin % 10000 == 0):
        #     print('calculate ',current_bin,' bins')
# print(clr.chromsizes[1])
for i in range(23):
    chrm_coverage[i] = int(chrm_coverage[i]) / clr.chromsizes[i]
print(chrm_coverage)
