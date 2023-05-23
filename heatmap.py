import numpy as np
import matplotlib.pyplot as plt

# Generate random data for 365 days.
data = np.random.randint(0, 11, (365,))

# Reshape data to have 7 columns, representing days of the week.
reshaped_data = np.reshape(data, (-1, 7))

# Create a figure and a set of subplots.
fig, ax = plt.subplots()

# Create the heatmap.
cax = ax.matshow(reshaped_data, cmap='hot')

# Create a colorbar for the heatmap. The colorbar will show how the colors correspond to values.
fig.colorbar(cax)

# Display the heatmap.
plt.show()
