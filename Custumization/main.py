import matplotlib.pyplot as plt

year = [1951, 1961, 1971, 1981, 1991, 2001, 2011]
pop = [2.58, 3.09, 3.77, 4.54, 5.41, 6.22, 7.04]

year = [1800, 1850, 1900] + year
pop = [1.0, 1.26, 1.65] + pop

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt .grid(True)

plt.yticks([0, 2, 4, 6, 8],
           ['B', '2B', '4B', '6B', '8B'])

plt.show()
