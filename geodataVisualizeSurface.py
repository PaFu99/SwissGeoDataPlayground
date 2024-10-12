import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial import Delaunay

# Function to read the coordinates from an .xyz file
def read_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Skip the header (X Y Z)
        x, y, z = [], [], []
        
        for line in lines:
            coords = line.split()
            x.append(float(coords[0]))
            y.append(float(coords[1]))
            z.append(float(coords[2]))
    
    return np.array(x), np.array(y), np.array(z)

# Filepath to the .xyz file
filename = 'SWISSALTI3D_10_XYZ_CHLV95_LN02_2600_1197.xyz'  # Replace with your file path

# Read the coordinates
x, y, z = read_coordinates(filename)

# Perform Delaunay triangulation on the x and y coordinates
points2D = np.column_stack((x, y))
tri = Delaunay(points2D)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface by connecting the dots using the triangulation
ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap='terrain', edgecolor='none')

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')

# Show plot
plt.show()
