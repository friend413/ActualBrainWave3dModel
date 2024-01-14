import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
from stl import mesh
import requests

# Function to fetch or simulate brain wave data
def fetch_brain_wave_data():
    # url = url_entry.get()
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()

    #     # Parse the data from the server
    #     # This is just a placeholder - you need to adapt this based on your server's data format
    #     data = response.json()
    #     x = np.array(data['x'])
    #     y = np.array(data['y'])
    #     z = np.array(data['z'])
    #     return x, y, z
    # except requests.RequestException as e:
    #     print(f"Error fetching data: {e}")
    #     return None, None, None

    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin( x ) + 3.5
    print(y)
    # x, y = np.meshgrid(x, y)
    # z = np.sin(np.sqrt(x**2 + y**2))
    z = np.sin( ( x - x ) + np.pi / 2 )
    # Sample data
    # x = [1, 2, 3, 4, 5]
    # y = [2, 3, 4, 5, 6]
    # z = [3, 4, 5, 6, 7]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, zs=0, zdir='z', label='Outer Circular Base')


    # Show the plot
    plt.show()
    return x, y, z

# Function to plot brain wave
def plot_brain_wave():
    x, y, z = fetch_brain_wave_data()

    # Create a 3D plot
    fig = plt.Figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    # Update the canvas
    canvas.get_tk_widget().pack_forget()
    canvas.__init__(fig, master=root)  # Re-initialize canvas
    canvas.draw()
    canvas.get_tk_widget().pack(padx=10, pady=10)

# Function to save the current plot as STL
def save_as_stl():
    x, y, z = fetch_brain_wave_data()
    num_cells = len(x) * len(y)
    vertices = np.zeros((num_cells, 3))
    faces = []

    for i in range(len(x)):
        for j in range(len(y)):
            vertices[i * len(y) + j] = [x[i, j], y[i, j], z[i, j]]
            if i < len(x) - 1 and j < len(y) - 1:
                faces.append([i * len(y) + j, (i+1) * len(y) + j, i * len(y) + j+1])
                faces.append([(i+1) * len(y) + j, (i+1) * len(y) + j+1, i * len(y) + j+1])

    brain_wave_mesh = mesh.Mesh(np.zeros(len(faces), dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            brain_wave_mesh.vectors[i][j] = vertices[f[j]]

    # File dialog for saving the file
    file_path = filedialog.asksaveasfilename(defaultextension=".stl", filetypes=[("STL files", "*.stl")])
    if file_path:
        brain_wave_mesh.save(file_path)

# Exit application
def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Brain Wave Visualizer")

# URL Entry Field
url_entry = tk.Entry(root, width=50)
url_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

# Fetch and Plot button
fetch_button = tk.Button(root, text="Fetch and Plot Brain Wave", command=plot_brain_wave)
fetch_button.pack(side=tk.TOP, pady=5)

# Save as STL button
save_button = tk.Button(root, text="Save as STL", command=save_as_stl)
save_button.pack(side=tk.TOP, pady=5)

# Canvas for matplotlib plot
fig = plt.Figure()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=10, pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
