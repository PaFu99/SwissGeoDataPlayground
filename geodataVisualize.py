import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to read the coordinates from a text file
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

# Filepath to the .txt file
filename = 'SWISSALTI3D_10_XYZ_CHLV95_LN02_2600_1197.xyz'  # Replace this with the path to your .txt file

# Read the coordinates
x, y, z = read_coordinates(filename)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='b', marker='o')

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')

# Show plot
plt.show()
