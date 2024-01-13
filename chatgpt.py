import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from stl import mesh

# Generate coordinates
diameter = 10
height = 10
resolution = 100

theta = np.linspace(0, 2 * np.pi, resolution)
z = np.linspace(0, height, resolution)
r = np.linspace(5, diameter/2, resolution) 

z, theta = np.meshgrid(z, theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot 3D brain wave model
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, alpha=0.7)

# Save the 3D model to an STL file
your_mesh = mesh.Mesh(np.zeros(x.shape[0], dtype=mesh.Mesh.dtype))
for i in range(x.shape[0]):
    your_mesh.vectors[i] = np.column_stack([x[i], y[i], z[i]])
your_mesh.save('brain_wave_model.stl')
