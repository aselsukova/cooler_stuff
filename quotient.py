import cooler
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

health = pd.read_csv(sys.argv[1] + '.csv',index_col=0)
health = np.log10(health)
n=24
if(sys.argv[1][1]=='X'):
    health.drop('chrY', axis=1, inplace=True)
    health.drop('chrY', axis=0, inplace=True)
    n=23
for i in range(n):
    health.iat[i, i] = 0
print(health)
disease = pd.read_csv(sys.argv[2] + '.csv',index_col=0)
disease = np.log10(disease)
if(sys.argv[1][1]=='X'):
    disease.drop('chrY', axis=1, inplace=True)
    disease.drop('chrY', axis=0, inplace=True)
for i in range(n):
    disease.iat[i, i] = 0
print(disease)
quotient = disease.astype('int32')/health.astype('float')
plt.cla()
print(quotient)
fig = sns.heatmap(data=quotient,cmap='coolwarm')
fig.figure.savefig(sys.argv[2] + '_quo.png')
