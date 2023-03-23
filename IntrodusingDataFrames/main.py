import pandas as pd
data = pd.read_csv('homelessness.csv')

# Print the head of the homelessness data
print(data.head())

# Print information about homelessness
print(data.info())

# Print the shape of homelessness
print(data.shape)

# Print the values of homelessness
print(data.values)

# Print the column index of homelessness
print(data.columns)

# Print the row index of homelessness
print(data.index)
