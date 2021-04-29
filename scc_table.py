import cooler
import sys
import pandas as pd

clr1 = cooler.Cooler(sys.argv[1])
clr2 = cooler.Cooler(sys.argv[2])
bins1 = pd.DataFrame(clr1.bins()[:])
bins2 = pd.DataFrame(clr2.bins()[:])
bins1.drop('chrom',axis=1,inplace=True)
bins2.drop('chrom',axis=1,inplace=True)
bins1.drop('weight',axis=1,inplace=True)
bins2.drop('weight',axis=1,inplace=True)
new_columns = ['contact_st','contact_en']
bins1.columns = new_columns
contacts1 = pd.DataFrame(clr1.matrix(as_pixels=True, join=True)[:,:])['count']
print(contacts1)
contacts2 = pd.DataFrame(clr2.matrix(as_pixels=True, join=True)[:,:])['count']
bins1['contact_count']=contacts1
print(bins1)
bins1['0']=contacts2
bins1.fillna(value=1,inplace=True)
print(bins1)
bins1.to_csv(sys.argv[1][:-5]+'-'+sys.argv[2][:-5],sep=' ',index=False)