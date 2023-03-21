
fam = [1.73, 1.68, 1.71, 1.89]
for height in fam:
    print(height)

for index, height in enumerate(fam):
    print('index ' + str(index) + ': ' + str(height))

for c in "family":
    print(c.capitalize())


# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas):
    print('room ' + str(index + 1) + ': ' + str(a))

# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room, area in house:
    print("the {} is {} sqm".format(room, area))

