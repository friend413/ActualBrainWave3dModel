import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Parameters
thickness = 5    
inner_diam = 5      
outer_diam = 10
num_points = 100

# Generate cylinder mesh
theta = np.linspace(0, 2*np.pi, num_points)     
z = np.linspace(-thickness/2, thickness/2, 10) 

r_inner = inner_diam/2   
r_outer = outer_diam/2

# Sample wave data     
left_waves = 0.5*np.sin(3*theta)      
right_waves = 0.7*np.cos(2*theta) 

x = None
y = None
z = None

def add_brainwave_data(left, right):

  global x, y, z

  x_left = r_inner*np.cos(theta)      
  y_left = r_inner*np.sin(theta)
  z_left = z.reshape(-1)    

  x_right = r_outer*np.cos(theta) + right 
  y_right = r_outer*np.sin(theta)
  z_right = z.reshape(-1)     

  x = np.concatenate((x_left, x_right))
  y = np.concatenate((y_left, y_right)) 
  z = np.concatenate((z_left, z_right))

 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
add_brainwave_data(left_waves, right_waves)
ax.plot_surface(x, y, z)
plt.show()