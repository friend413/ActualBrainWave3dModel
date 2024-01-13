import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Define the circle parameters
center = (0, 0)
radius = 1

# Create an array of theta values for the circle
theta = np.linspace(0, 2 * np.pi, 100)

# Calculate the x and y coordinates of the circle
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# Plot the circle
ax.plot(x, y, label='Circle')

# Set aspect ratio to be equal, so the circle looks like a circle
ax.set_aspect('equal', adjustable='box')

# Add labels and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Circle in Python')
ax.legend()

# Show the plot
plt.show()