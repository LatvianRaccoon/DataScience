import pandas as pd
import numpy as np

brics = pd.read_csv('brics.csv', index_col=0)

for lab, row in brics.iterrows():
    print(lab)
    print(row)

print()

for lab, row in brics.iterrows():
    print('{}: {}'.format(lab, row['capital']))

print()

for lab, row in brics.iterrows():
    brics.loc[lab, 'name_length'] = len(row['country'])
print(brics)

brics['name_length'] = brics['country'].apply(len)
print(brics)
