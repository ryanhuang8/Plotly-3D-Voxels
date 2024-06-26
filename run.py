import plotly.graph_objects as go
import dash
from dash import dcc, html
import numpy as np
from VoxelData import VoxelData

# Sample voxel data for testing
voxel_data = np.load("chair.npy")[1][0].astype(int)

app = dash.Dash(__name__)

# Process the voxel data
voxels = VoxelData(voxel_data)
vertices, faces = voxels.get_vertices_and_faces()

# Flatten vertices and faces arrays for Plotly
vertices = np.array(vertices)
x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
faces = np.array(faces)
i, j, k = faces[:, 0], faces[:, 1], faces[:, 2]

fig_3d = go.Figure(data=[
    go.Mesh3d(
        x=x, y=y, z=z,
        i=i, j=j, k=k,
        opacity=1
    )
])

app.layout = html.Div([
    dcc.Graph(id='graph-3d-mesh', figure=fig_3d)
])

if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
