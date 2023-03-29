'''
for i in range(7):
    ro = taxi_owners.loc[i, :].values.flatten().tolist()

    result = ''
    for j in ro:
        result += str(j).replace(',', '') + ","
    result = result.rstrip(',')
    print(result.strip())
'''