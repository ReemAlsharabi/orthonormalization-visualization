# Orthonormalization Visualization
This program uses the Plotly library to create an interactive 3D scatter plot that visualizes the relationship between input vectors and their orthonormal counterparts. The user can adjust the angle of the vectors using sliders, and the program will update the plot to show the input vectors in blue and the orthonormal vectors in red.

![alt text](https://github.com/ReemAlsharabi/orthonormalization-visualization/blob/main/v.gif)

## Functionality
* The _orthogonalize_ function takes in a list of vectors and returns a new list of orthonormal vectors by applying the Gram-Schmidt process.
* The _update_plots_ function creates the plot and uses the interact function from the ipywidgets library to create sliders that allow the user to adjust the angle of the vectors.
* The angles are then used to create the input vectors, which are then passed through the _orthogonalize_ function to get the orthonormal vectors.
* These vectors are then plotted in 3D space using Plotly, with input vectors in blue and orthonormal vectors in red. The final line of code displays the interactive plot using the _show_ method of the figure object.

## Requirements
This program requires the following python libraries:* plotly
* numpy
* plotly
* ipywidgets

# Usage
To run this program, simply execute the code. This will open an interactive plot that allows you to adjust the angles of the vectors and see the corresponding orthonormal vectors in real-time.

_You can run the program using the command below:_

```python3 main.py```

## Conclusion
This program can be used to visualize the relationship between input vectors and their orthonormal counterparts, and is useful for understanding the Gram-Schmidt process and orthonormal vectors. The interactive nature of the plot allows for easy experimentation and understanding of the underlying concepts.
