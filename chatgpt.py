import numpy as np
from stl import mesh

def generate_cylinder_model():
    # Cylinder dimensions
    inner_diameter = 5
    outer_diameter = 10
    height = 100

    # Generate waveform data (replace with your actual brain wave waveform data)
    waveform = np.sin(np.linspace(0, 2*np.pi, 100))

    # Calculate number of points on the perimeter
    num_points = len(waveform)
    
    # Calculate the coordinates of the points on the perimeter
    theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
    x = (outer_diameter/2) * np.cos(theta)
    y = (outer_diameter/2) * np.sin(theta)
    z = (waveform * 2) + (outer_diameter/2)
    
    # Create the STL mesh
    vertices = np.column_stack((x, y, z))
    faces = []
    for i in range(num_points-1):
        faces.append([i, i+1, num_points+i+1])
        faces.append([i, num_points+i+1, num_points+i])
    faces.append([num_points-1, 0, num_points])
    faces.append([num_points-1, num_points, 2*num_points-1])
    
    # Create the mesh object
    mesh_data = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = vertices[f[j]]
    
    # Save the mesh as STL file
    mesh_data.save('cylinder.stl')

# Generate the cylinder model
generate_cylinder_model()