import plotly.graph_objects as go
import numpy as np
from stl import mesh

# Input Data & you should change this part
alpha = np.linspace( 0, 10*np.pi, 100 )
rdata = np.sin( alpha ) # you should input right data
ldata = np.sin( alpha ) # you should input left data

inner_radius = 2.5
middle_line = 4 # you should change this but if you change this value to 3.5, that 3d model can be easily broke. so i recommend this value as 4.

# Define vertices

rx = []
ry = []
rz = []
ri = []
rj = []
rk = []

data = np.append( ldata, np.flip(rdata) )
length = len( data )
theta = np.linspace( np.pi / 2, - 3 * np.pi / 2, length )

for index in range(length):
    rx.append( ( middle_line + data[index] ) * np.cos( theta[index] ) ) # index
    ry.append( ( middle_line + data[index] ) * np.sin( theta[index] ) )
    rz.append( 0.5 )

    rx.append( ( middle_line + data[index] ) * np.cos( theta[index] ) ) # index + 1
    ry.append( ( middle_line + data[index] ) * np.sin( theta[index] ) )
    rz.append( 0.0 )

    rx.append( ( inner_radius ) * np.cos( theta[index] ) ) # index + 2
    ry.append( ( inner_radius ) * np.sin( theta[index] ) )
    rz.append( 0.0 )

    rx.append( ( inner_radius ) * np.cos( theta[index] ) ) # index + 3
    ry.append( ( inner_radius ) * np.sin( theta[index] ) )
    rz.append( 0.5 )

    if index >= 1:
        ri.append( 4 * index )
        ri.append( 4 * index )
        ri.append( 4 * index )
        ri.append( 4 * index )
        ri.append( 4 * index + 2 )
        ri.append( 4 * index + 2 )
        ri.append( 4 * index + 2 )
        ri.append( 4 * index + 2 )

        rj.append( 4 * index - 4 )
        rj.append( 4 * index - 1 )
        rj.append( 4 * index - 4 )
        rj.append( 4 * index - 3 )
        rj.append( 4 * index + 1 )
        rj.append( 4 * index - 2 )
        rj.append( 4 * index - 2 )
        rj.append( 4 * index + 3 )

        rk.append( 4 * index - 1 )
        rk.append( 4 * index + 3 )
        rk.append( 4 * index - 3 )
        rk.append( 4 * index + 1 )
        rk.append( 4 * index - 3 )
        rk.append( 4 * index - 3 )
        rk.append( 4 * index - 1 )
        rk.append( 4 * index - 1 )

# Create the mesh
meshObj = go.Mesh3d(x=rx, y=ry, z=rz, i=ri, j=rj, k=rk, opacity=0.5)

# Define the layout and plot
fig = go.Figure(data=[meshObj])
fig.update_layout(scene=dict(xaxis_title='X Axis',
                             yaxis_title='Y Axis',
                             zaxis_title='Z Axis'))
fig.show()

vertices = np.array([[rx[n], ry[n], rz[n]] for n in range(len(rx))])

# Convert to faces
faces = np.array([[ri[n], rj[n], rk[n]] for n in range(len(ri))])

# Create the mesh
mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

for i, f in enumerate(faces):
    for j in range(3):
        mesh_data.vectors[i][j] = vertices[f[j],:]

# Save the mesh as an STL file
mesh_data.save('my_mesh.stl')
