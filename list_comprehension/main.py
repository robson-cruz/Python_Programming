# Challenge 5: Turning a matrix into a single list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

print([element for row in matrix for element in row])
