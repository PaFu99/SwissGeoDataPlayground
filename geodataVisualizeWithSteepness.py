import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

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
    
    return x, y, z

# Function to calculate the terrain steepness
def calculate_steepness(x, y, z):
    steepness = []
    for i in range(1, len(x)):
        # Calculate the horizontal distance between two points (Euclidean distance in the XY plane)
        horizontal_distance = np.sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
        
        # Calculate the vertical distance (Z difference)
        vertical_distance = z[i] - z[i-1]
        
        # Calculate the slope (rise over run)
        slope = np.arctan2(vertical_distance, horizontal_distance)  # Gives result in radians
        steepness.append(np.degrees(slope))  # Convert to degrees
    
    # Add a zero steepness for the first point (no prior point)
    steepness.insert(0, 0)
    return np.array(steepness)

# Filepath to the .xyz file
filename = 'SWISSALTI3D_10_XYZ_CHLV95_LN02_2600_1197.xyz'  # Replace this with the path to your .xyz file

# Read the coordinates
x, y, z = read_coordinates(filename)

# Calculate the steepness of the terrain
steepness = calculate_steepness(x, y, z)

# Normalize steepness for coloring (steepest is dark, flattest is bright)
norm_steepness = (steepness - np.min(steepness)) / (np.max(steepness) - np.min(steepness))

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Apply the RdYlGn colormap where red represents steep and green represents flat terrain
colors = plt.cm.RdYlGn(1 - norm_steepness)

# Plot the terrain with colors based on steepness
sc = ax.scatter(x, y, z, c=colors)

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')

# Add a color bar to represent steepness visually
cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Steepness (degrees)')

# Show plot
plt.show()
