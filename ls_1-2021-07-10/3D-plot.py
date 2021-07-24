"""
	Plotting the 3D terrain generated my game_of_life
"""
import game_of_life as gol

from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

# GETTING THE HEIGHTS
heights = gol.generateMaps()

# INITIALISING THE PLOT
fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111, projection = "3d")

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
z = []

for i in range(100):
	z.append(heights[i])

z = np.array(z)
X, Y = np.meshgrid(x, y)

Z = np.array(heights)

# APPLYING THE GAUSSIAN SMOOTHENING
Z = gaussian_filter(Z, sigma=2)

# PLOTTING THE TERRAIN
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='twilight', edgecolor='None')
ax.set_zlim3d(0, 10)
ax.set_xlim3d(0,10)
ax.set_ylim3d(0,10)

plt.show()