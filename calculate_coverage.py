import cooler
from cooltools import coverage
import sys

clr = cooler.Cooler(sys.argv[1])
cis, total = coverage.get_coverage(clr,  ignore_diags = 1)