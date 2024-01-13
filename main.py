import numpy as np
import requests
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from stl import mesh

# Initialize Variables

outer_radius = 5
inner_radius = 2.5
height = 0.5
# server_url  = "https://brainwave.com/api/data"
server_url = "https://business-card-maker-6c95b-default-rtdb.firebaseio.com/global.json"

# Input Data

response = requests.get( server_url )

if response.status_code == 200:
    data = response.json()
    brain_wave_data = data["brain_wave"]
    
else:
    print("Failed to retireve data, Status code", response.status_code)

# Main View

