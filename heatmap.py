import numpy as np
import matplotlib.pyplot as plt
import datetime

# Get today's date.
today = datetime.date.today()

# Calculate the start date, one year ago from today.
start_date = today - datetime.timedelta(days=365)

# Calculate how many days are between the start date and the nearest Sunday (0 represents Monday, 6 represents Sunday).
padding_start = (start_date.weekday() + 1) % 7

# Calculate how many days are between today and the nearest Saturday.
padding_end = (6 - today.weekday()) % 7

# Generate random data for each day of the past year.
data = np.random.randint(0, 11, (365,))

# Calculate the total padding to make the data length divisible by 7.
total_padding = padding_start + padding_end

# Append the missing values to the data.
data = np.pad(data, (padding_start, padding_end), 'constant')

# Reshape data to have 7 rows, representing days of the week.
reshaped_data = np.reshape(data, (-1, 7)).T

# Create a figure and a set of subplots.
fig, ax = plt.subplots()

# Create the heatmap.
cax = ax.matshow(reshaped_data, cmap='Blues')

# Hide y-tick labels.
ax.set_yticks([])

# Display the heatmap.
plt.show()
