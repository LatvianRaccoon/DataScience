import pandas as pd


temperatures = pd.read_csv('temperatures.csv')

# Add a year column to temperatures
temperatures['date'] = pd.to_datetime(temperatures['date'], errors='coerce')
temperatures['year'] = temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country', 'city'],  columns='year')

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt': 'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): ('India', 'Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): ('India', 'Delhi'), '2005': '2010'])

# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
