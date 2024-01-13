import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh

# Cylinder parameters
inner_radius = 2.5  # in centimeters
outer_radius = 5  # in centimeters
height = 0.5  # in centimeters

# Create theta values for the circular base
theta = np.linspace(0, 2 * np.pi, 100)

# Create points for the outer circular base
x_outer = outer_radius * np.cos(theta)
y_outer = outer_radius * np.sin(theta)

# Create points for the inner circular base
x_inner = inner_radius * np.cos(theta)
y_inner = inner_radius * np.sin(theta)

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the outer circular base
ax.plot(x_outer, y_outer, zs=0, zdir='z', label='Outer Circular Base')

# Plot the inner circular base
ax.plot(x_inner, y_inner, zs=0, zdir='z', label='Inner Circular Base')

# Plot the outer and inner vertical lines connecting the bases
for i in range(len(theta)):
    ax.plot([x_outer[i], x_inner[i]], [y_outer[i], y_inner[i]], [0, 0], color='black')

# Plot the outer and inner circular tops at the specified height
ax.plot(x_outer, y_outer, zs=height, zdir='z', label='Outer Circular Top')
ax.plot(x_inner, y_inner, zs=height, zdir='z', label='Inner Circular Top')

# Plot the vertical lines connecting the outer and inner tops
for i in range(len(theta)):
    ax.plot([x_outer[i], x_inner[i]], [y_outer[i], y_inner[i]], [height, height], color='black')

# Set axis labels and title
ax.set_xlabel('X-axis (cm)')
ax.set_ylabel('Y-axis (cm)')
ax.set_zlabel('Z-axis (cm)')
ax.set_title('3D Cylinder with Inner and Outer Radii')

# Add legend
ax.legend()

# Show the plot
plt.show()

# Save the cylinder as an STL file
your_mesh = mesh.Mesh(np.zeros(2 * len(theta) * 2, dtype=mesh.Mesh.dtype))

# Add vertices for the outer circular base
for i in range(len(theta)):
    your_mesh.vectors[i] = [x_outer[i], y_outer[i], 0]

# Add vertices for the inner circular base
for i in range(len(theta)):
    your_mesh.vectors[len(theta) + i] = [x_inner[i], y_inner[i], 0]

# Add vertices for the outer circular top
for i in range(len(theta)):
    your_mesh.vectors[2 * len(theta) + i] = [x_outer[i], y_outer[i], height]

# Add vertices for the inner circular top
for i in range(len(theta)):
    your_mesh.vectors[3 * len(theta) + i] = [x_inner[i], y_inner[i], height]

# Save the STL file
your_mesh.save('cylinder.stl')
