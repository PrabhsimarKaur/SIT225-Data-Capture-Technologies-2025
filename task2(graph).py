import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('sensor_data.csv')

# Display the first few rows to check the data
df.head()

# Create a figure and axes for two subplots
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot Temperature on the first axis (left y-axis)
color = 'tab:blue'
ax1.set_xlabel('Timestamp')
ax1.set_ylabel('Temperature (°C)', color=color)
ax1.plot(df['Timestamp'], df['Temperature (C)'], color=color, label='Temperature', marker='o')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_title('Temperature and Humidity Variation')

# Create a second y-axis to plot Humidity (on the right)
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Humidity (%)', color=color)
ax2.plot(df['Timestamp'], df['Humidity (%)'], color=color, label='Humidity', marker='x')
ax2.tick_params(axis='y', labelcolor=color)

# Show the grid and the legend
ax1.grid(True)
fig.tight_layout()

# Show the plot
plt.show()
