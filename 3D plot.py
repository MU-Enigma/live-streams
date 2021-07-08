import matplotlib

import game_of_life as gol

from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import mpl_toolkits
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

heights = gol.generateMaps()

fig = plt.figure(figsize = (7,7))
ax = fig.add_subplot(111, projection = "3d")

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
z = []

for i in range(100):
  z.append(heights[i])
z = np.array(z)
X, Y = np.meshgrid(x, y)
# X, Z = np.meshgrid(x, z)
# Y, Z = np.meshgrid(y, z)
Z = np.array(heights)
Z = gaussian_filter(Z, sigma=2)
# ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='twilight', edgecolor='None')
ax.set_zlim3d(0, 10)
ax.set_xlim3d(0,10)
ax.set_ylim3d(0,10)
# ax.view_init(50, 20)

plt.show()