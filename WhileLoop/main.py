error = 50.0

while error > 1:
    error = error / 4
    print(error)

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset -= 1
    print(offset)

print()
print()

# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset -= 1
    else:
        offset += 1
    print(offset)
