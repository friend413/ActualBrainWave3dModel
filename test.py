from stl import mesh
import numpy as np

x = [0,1,2,0]
y = [0,2,0,1]
z = [1,1,1,2]

i = [0,0,0]
j = [1,2,1]
k = [2,3,3]

vertices = np.array([[x[n], y[n], z[n]] for n in range(len(x))])

# Convert to faces
faces = np.array([[i[n], j[n], k[n]] for n in range(len(i))])

# Create the mesh
mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

for i, f in enumerate(faces):
    for j in range(3):
        mesh_data.vectors[i][j] = vertices[f[j],:]

# Save the mesh as an STL file
mesh_data.save('my_mesh.stl')
