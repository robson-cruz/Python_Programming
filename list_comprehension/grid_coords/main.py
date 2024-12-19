# Create a list containing all possible coordinates in a 2D grid from 0 to 2 (including).
# Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print([(x, y) for x in range(3) for y in range(3)])
