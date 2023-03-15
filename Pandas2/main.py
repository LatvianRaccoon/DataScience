
import pandas as pd

brics = pd.read_csv('brics.csv', index_col=0)
print(brics)
print()
print(brics['country'])
print()
print(brics[['country']])
print()
print(brics[['country', 'capital']])
print()
print(brics[1:4])
print()
print(brics.loc['RU'])
print()
print(brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']])
print()
print(brics.loc[:, ['country', 'capital']])

