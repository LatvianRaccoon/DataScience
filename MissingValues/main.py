import pickle
import pandas as pd
import matplotlib.pyplot as plt


pkl_file = open('avoplotto.pkl', 'rb')
avocados = pickle.load(pkl_file)

# Check individual values for missing values
print(avocados.isna())

# Check each column for missing values
print(avocados.isna().any())

# Bar plot of missing values by variable
avocados.isna().sum().plot(kind='bar')

# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())
