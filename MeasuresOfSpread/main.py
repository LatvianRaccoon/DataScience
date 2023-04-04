import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

food_consumption = pd.read_csv('food_consumption.csv')

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 5)))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))


# Create histogram of co2_emission for food_category 'beef'
beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']
plt.hist(beef_consumption['co2_emission'])
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
beef_consumption = food_consumption[food_consumption['food_category'] == 'eggs']
plt.hist(beef_consumption['co2_emission'])
# Show plot
plt.show()

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)


