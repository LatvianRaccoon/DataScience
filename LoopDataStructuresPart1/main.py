import numpy as np

world = {'afghanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}

for key, value in world.items():
    print(key + ' -- ' + str(value))

print()

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
bmi = np_weight / np_height ** 2

for val in bmi:
    print(val)

print()

for val in meas:
    print(val)

print()

for val in np.nditer(meas):
    print(val)

print()

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of {} is {}".format(key, value))

print()

