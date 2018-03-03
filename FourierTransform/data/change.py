import pandas as pd
import numpy as np


fname1 = 'sunspot.dat'
t01 = 1748
dt1 = 0.25
fname2 = 'sst_nino3.dat'
t02=1871
dt2=0.25


df2 = pd.DataFrame()
df3 = pd.DataFrame()


d2 = np.loadtxt(fname1)
d3 = np.loadtxt(fname2)



N2 = d2.size
N3 = d3.size

t1 = np.zeros(N2)
t2 = np.zeros(N3)



i2 = 0
i3 = 0



for x in range(0, N2):
	t1[i2] = t01
	t01 += dt1
	i2+=1

for x in range(0, N3):
	t2[i3] = t02
	t02 += dt2
	i3+=1

df2['t'] = t1
df2['f'] = d2

df3['t'] = t2
df3['f'] = d3


df2.to_csv('sunspot.csv', sep=',', encoding='utf-8', index=False, header = False)
df3.to_csv('nino3.csv', sep=',', encoding='utf-8', index=False, header = False)