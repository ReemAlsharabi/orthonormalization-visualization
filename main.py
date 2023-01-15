import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import interact, fixed, widgets
import numpy as np

def orthogonalize(vectors):
    orthonormal = []
    for v in vectors:
        w = v - sum(np.dot(v, u) / np.dot(u, u) * u for u in orthonormal)
        orthonormal.append(w / np.linalg.norm(w))
    return orthonormal

def update_plots(angle1, angle2, angle3):
    vectors = np.array([[np.cos(angle1), np.sin(angle1), 0],
                       [np.cos(angle2), 0, np.sin(angle2)],
                       [0, np.cos(angle3), np.sin(angle3)]])

    orthonormal = orthogonalize(vectors)

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter3d'}]])

    for i in range(len(vectors)):
        fig.add_trace(go.Scatter3d(x=[0, vectors[i][0]], y=[0, vectors[i][1]], z=[0, vectors[i][2]],
                                   mode='lines', line=dict(color='blue', width=2)))
        fig.add_trace(go.Scatter3d(x=[0, orthonormal[i][0]], y=[0, orthonormal[i][1]], z=[0, orthonormal[i][2]],
                                   mode='lines', line=dict(color='red', width=2)))
    fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'), showlegend=False)
    fig.show()

interact(update_plots, angle1=widgets.FloatSlider(min=0, max=2*np.pi, step=0.1, value=0), angle2=widgets.FloatSlider(min=0, max=2*np.pi, step=0.1, value=0), angle3=widgets.FloatSlider(min=0, max=2*np.pi, step=0.1, value=0))

"""
This code uses the Plotly library to create a 3D scatter plot that visualizes the relationship between input vectors and their orthonormal counterparts.
The orthogonalize function takes in a list of vectors and returns a new list of orthonormal vectors by applying the Gram-Schmidt process.
The update_plots function creates the plot and uses the interact function from the ipywidgets library to create sliders that allow the user to adjust the angle of the vectors.
The angles are then used to create the input vectors, which are then passed through the orthogonalize function to get the orthonormal vectors.
These vectors are then plotted in 3D space using Plotly, with input vectors in blue and orthonormal vectors in red. The final line of code displays the interactive plot using the show method of the figure object.
"""
