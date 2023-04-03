import pandas as pd

gdp = pd.read_csv('gdp.csv')
sp500 = pd.read_csv('sp500.csv')

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', right_on='Date', how='left', fill_method='ffill')


# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['GDP', 'Returns']]


# Print gdp_sp500
print(gdp_returns.corr())
