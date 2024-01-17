import plotly.graph_objects as go
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import os
import vtk

# Input Data & you should change this part
rdata = [0.3, 0.18, 0.58, 0.86, 0.96, 0.58, 0.86, 0.18, 0.22, 0.85, 0.58, 0.16, 0.07, 0.44, 0.75, 0.19, 0.7, 0.59, 0.32, 0.97, 0.12, 0.57, 0.01, 0.19, 0.12, 0.8, 0.87, 0.37, 0.93, 0.71, 0.64, 0.23, 0.46, 0.6, 0.08, 0.27, 0.88, 0.04, 0.75, 0.76, 0.9, 0.66, 0.17, 0.79, 0.95, 0.58, 0.26, 0.83, 0.96, 0.28, 0.2, 0.25, 0.29, 0.6, 0.39, 0.77, 0.64, 0.14, 0.61, 0.16, 0.34, 0.71, 0.26, 0.22, 0.01, 0.93, 0.65, 0.2, 0.48, 0.73, 0.01, 0.5, 0.45, 0.42, 0.21, 0.38, 0.64, 0.71, 0.07, 0.3, 0.0, 0.34, 0.94, 0.87, 0.93, 0.61, 0.21, 0.62, 0.72, 0.02, 0.33, 0.24, 0.83, 0.41, 0.99, 0.86, 0.06, 0.28, 0.47, 0.15]

ldata = [0.3, 0.18, 0.58, 0.86, 0.96, 0.58, 0.86, 0.18, 0.22, 0.85, 0.58, 0.16, 0.07, 0.44, 0.75, 0.19, 0.7, 0.59, 0.32, 0.97, 0.12, 0.57, 0.01, 0.19, 0.12, 0.8, 0.87, 0.37, 0.93, 0.71, 0.64, 0.23, 0.46, 0.6, 0.08, 0.27, 0.88, 0.04, 0.75, 0.76, 0.9, 0.66, 0.17, 0.79, 0.95, 0.58, 0.26, 0.83, 0.96, 0.28, 0.2, 0.25, 0.29, 0.6, 0.39, 0.77, 0.64, 0.14, 0.61, 0.16, 0.34, 0.71, 0.26, 0.22, 0.01, 0.93, 0.65, 0.2, 0.48, 0.73, 0.01, 0.5, 0.45, 0.42, 0.21, 0.38, 0.64, 0.71, 0.07, 0.3, 0.0, 0.34, 0.94, 0.87, 0.93, 0.61, 0.21, 0.62, 0.72, 0.02, 0.33, 0.24, 0.83, 0.41, 0.99, 0.86, 0.06, 0.28, 0.47, 0.15]


inner_radius = 2.5
middle_line = 4 # you should change this but if you set this value to 3.5, that 3d model can be easily broke in case of -1 value. so i recommend this value as 4.
separation_angle = np.pi / 75 # you should change this

# Define vertices

rx = []
ry = []
rz = []
ri = []
rj = []
rk = []

rdata = np.append(np.append( 0, rdata ), 0)
ldata = np.append(np.append( 0, ldata ), 0)

rlength = len( rdata )
llength = len( ldata )

data = np.append( rdata, np.flip(ldata) )

# data = np.append( data, rdata[0] )
length = rlength + llength
theta = np.linspace( np.pi / 2, - np.pi / 2, rlength )
theta = np.append( theta, np.linspace( - np.pi / 2, -3 * np.pi / 2, llength ) )
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
# Maka a seperation line
# index = length + 1
# rx.append( 0 ) # index
# ry.append( middle_line )
# rz.append( 0.4 )

# rx.append( 0 ) # index + 1
# ry.append( middle_line )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( np.pi / 2 + separation_angle ) ) # index + 2
# ry.append( ( inner_radius ) * np.sin( np.pi / 2 + separation_angle ) )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( np.pi / 2 + separation_angle ) ) # index + 3
# ry.append( ( inner_radius ) * np.sin( np.pi / 2 + separation_angle ) )
# rz.append( 0.4 )

# rx.append( 0 ) # index
# ry.append( -middle_line )
# rz.append( 0.4 )

# rx.append( 0 ) # index + 1
# ry.append( -middle_line )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( -np.pi / 2 - separation_angle ) ) # index + 2
# ry.append( ( inner_radius ) * np.sin( -np.pi / 2 - separation_angle ) )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( -np.pi / 2 - separation_angle ) ) # index + 3
# ry.append( ( inner_radius ) * np.sin( -np.pi / 2 - separation_angle ) )
# rz.append( 0.4 )

# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )

# rj.append( 4 * index - 4 )
# rj.append( 4 * index - 1 )
# rj.append( 4 * index - 4 )
# rj.append( 4 * index - 3 )
# rj.append( 4 * index + 1 )
# rj.append( 4 * index - 2 )
# rj.append( 4 * index - 2 )
# rj.append( 4 * index + 3 )

# rk.append( 4 * index - 1 )
# rk.append( 4 * index + 3 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index + 1 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index - 1 )
# rk.append( 4 * index - 1 )

# index = length + 3
# rx.append( 0 ) # index
# ry.append( middle_line )
# rz.append( 0.4 )

# rx.append( 0 ) # index + 1
# ry.append( middle_line )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( np.pi / 2 - separation_angle ) ) # index + 2
# ry.append( ( inner_radius ) * np.sin( np.pi / 2 - separation_angle ) )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( np.pi / 2 - separation_angle ) ) # index + 3
# ry.append( ( inner_radius ) * np.sin( np.pi / 2 - separation_angle ) )
# rz.append( 0.4 )

# rx.append( 0 ) # index
# ry.append( -middle_line )
# rz.append( 0.4 )

# rx.append( 0 ) # index + 1
# ry.append( -middle_line )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( -np.pi / 2 + separation_angle ) ) # index + 2
# ry.append( ( inner_radius ) * np.sin( -np.pi / 2 + separation_angle ) )
# rz.append( 0.1 )

# rx.append( ( inner_radius ) * np.cos( -np.pi / 2 + separation_angle ) ) # index + 3
# ry.append( ( inner_radius ) * np.sin( -np.pi / 2 + separation_angle ) )
# rz.append( 0.4 )

# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )
# ri.append( 4 * index + 2 )

# rj.append( 4 * index - 4 )
# rj.append( 4 * index - 1 )
# rj.append( 4 * index - 4 )
# rj.append( 4 * index - 3 )
# rj.append( 4 * index + 1 )
# rj.append( 4 * index - 2 )
# rj.append( 4 * index - 2 )
# rj.append( 4 * index + 3 )

# rk.append( 4 * index - 1 )
# rk.append( 4 * index + 3 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index + 1 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index - 3 )
# rk.append( 4 * index - 1 )
# rk.append( 4 * index - 1 )

        
# Create the mesh
meshObj = go.Mesh3d(x=rx, y=ry, z=rz, i=ri, j=rj, k=rk)

# fig = go.Figure(data=[meshObj])

text_mesh = mesh.Mesh.from_file('assets/asset.stl')
# fig.add_mesh3d(text_mesh.vectors)
# go.Mesh3d(text_mesh)
# fig.update_layout(scene=dict(xaxis_title='X Axis',
#                              yaxis_title='Y Axis',
#                              zaxis_title='Z Axis',
#                             xaxis=dict(range=[-5, 5]),  # Update axis ranges
#                             yaxis=dict(range=[-5, 5]),
#                             zaxis=dict(range=[-5, 5]),))
# fig.show()

vertices = np.array([[rx[n], ry[n], rz[n]] for n in range(len(rx))])

# Convert to faces
faces = np.array([[ri[n], rj[n], rk[n]] for n in range(len(ri))])

# Create the mesh
mesh_data = mesh.Mesh(np.zeros(faces.shape[0] + text_mesh.vectors.shape[0], dtype=mesh.Mesh.dtype))
org = faces.shape[0]

for i, f in enumerate(faces):
    for j in range(3):
        mesh_data.vectors[i][j] = vertices[f[j],:]
for i, f in enumerate( text_mesh.vectors ):
    for j in range(3):
        mesh_data.vectors[i + org ][j] = f[j]
# Save the mesh as an STL file
mesh_data.save('my_mesh.stl')

# View

reader = vtk.vtkSTLReader()
reader.SetFileName("my_mesh.stl")

mapper = vtk.vtkPolyDataMapper()

mapper.SetInputConnection(reader.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)
renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()

renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderer.AddActor(actor)
renderer.SetBackground(1, 1, 1) # Background color
renderWindow.Render()
renderWindowInteractor.Start() 