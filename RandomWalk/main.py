import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)
print()

tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)
print(tails)

random_walk = [0]

# Complete the
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
