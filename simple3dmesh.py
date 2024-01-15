import plotly.graph_objects as go
import numpy as np

# Download data set from plotly repo
# pts = np.loadtxt(np.DataSource().open('https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'))
# x, y, z = pts.T

theta = np.linspace(0, np.pi, 100)

x = []
y = []
z = []

for alpha in theta:
    x.append( 3.5 * np.cos( alpha ) )
    x.append( 2.5 * np.cos( alpha ) )
    y.append( 3.5 * np.sin( alpha ) )
    y.append( 2.5 * np.sin( alpha ) )
    z.append( 3.5 )
    z.append( 3.5 )
# tx = []
# ty = []
# tz = []
# for k in range(200):
#     tx.append( x[k] )
#     ty.append( y[k] )
#     tz.append( z[k] )
# print(tx)
fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=1)])
fig.show()