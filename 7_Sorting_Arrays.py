import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="#4CAF50")
plt.show()

# Sorting the arrays
sorted_indices = np.argsort(y)
sorted_y = y[sorted_indices]
sorted_x = x[sorted_indices]

plt.bar(sorted_x, sorted_y, color="#4CAF50")
plt.show()
