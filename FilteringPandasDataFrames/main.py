import pandas as pd
import numpy as np

brics = pd.read_csv('brics.csv', index_col=0)
print(brics)
print()

is_huge = brics.loc[:, 'area'] > 8
print(brics[is_huge])
print()

mid_areas = brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)]
print(mid_areas)


# Import cars data
cars = pd.read_csv('cars.csv', index_col=0)


# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars.loc[dr]

# Print sel
print(sel)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

cpc = cars['cars_per_cap']
# Create car_maniac: observations that have a cars_per_cap over 500
many_cars = cars['cars_per_cap'] > 500
car_maniac = cars[many_cars]


# Print car_maniac
print(car_maniac)
