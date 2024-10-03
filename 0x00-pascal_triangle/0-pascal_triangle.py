#!/usr/bin/python3
"""
pascal
"""

def pascal_triangle(n):
	"""
	Returns a list of lists of integers representing Pascal’s triangle of n
	"""
	triangle = []
	if n <= 0:
		return triangle

	triangle.append([1])  # Start the triangle with the first row

	for i in range(1, n):  # Loop to generate n rows
		row = [1]  # Start each row with the first element as 1

	for j in range(len(triangle[i - 1]) - 1):  # Calculate the inner elements
		row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])

	row.append(1)  # Append the last element as 1
	triangle.append(row)  # Add the constructed row to the triangle

	return triangle
