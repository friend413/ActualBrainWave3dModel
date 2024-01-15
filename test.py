import numpy as np
import matplotlib.pyplot as plt
# import surf2stl

# create x,y,z data for 3d surface plot
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')

plt.show()
# surf2stl.write('3d-sinusoidal.stl', X, Y, Z)