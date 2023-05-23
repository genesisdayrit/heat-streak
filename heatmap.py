import numpy as np
import matplotlib.pyplot as plt

# Generate random data for 365 days.
data = np.random.randint(0, 11, (365,))

# Calculate the number of missing values to make the data length divisible by 7.
padding = (7 - len(data) % 7) % 7

# Append the missing values to the data.
data = np.append(data, np.zeros(padding))

# Reshape data to have 7 columns, representing days of the week.
reshaped_data = np.reshape(data, (-1, 7))

# Create a figure and a set of subplots.
fig, ax = plt.subplots()

# Create the heatmap, transposing the data to rotate the heatmap 90 degrees.
cax = ax.matshow(reshaped_data.T, cmap='Blues')

# Hide y-tick labels.
ax.set_yticks([])

# Create a colorbar for the heatmap. The colorbar will show how the colors correspond to values.
fig.colorbar(cax)

# Display the heatmap.
plt.show()
