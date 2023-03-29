# Program prints out CSV format in IPython shell in DataCamp editor.
# You need just make copy and paste from IPython shell to text editor and save as csv file

'''
f = dataset name

for i in range(1):
    row = f.columns.tolist()

    result = ''
    for j in row:
        result += str(j).replace(',', '') + ","
    result = result.rstrip(',')
    print(result.strip())
for i in range(50):
    row = f.loc[i, :].values.flatten().tolist()

    result = ''
    for j in row:
        result += str(j).replace(',', '') + ","
    result = result.rstrip(',')
    print(result.strip())
'''