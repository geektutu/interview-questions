import numpy as np
import matplotlib.pyplot as plt

plt.axis([-3, 3, -3, 3])

points_a = np.array([(-1, 1), (1, -1), (-1, -1)])
points_b = np.array([(1, 1), (2, 0), (2, 1)])

plt.scatter(points_a[:,0], points_a[:,1], color='red', s=10**2)
plt.scatter(points_b[:,0], points_b[:,1], color='blue', s=10**2)

for _x, _y in np.concatenate([points_a, points_b]):
    plt.text(_x - 0.5, _y - 0.5, '({}, {})'.format(_x, _y), fontsize=16)

plt.show()
