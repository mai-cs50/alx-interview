def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal Triangle of n.
    Returns an empty list if n <= 0.
    """
    # Initialize the triangle
    triangle = []
    
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return triangle
    
    # Start with the first row of the triangle
    triangle.append([1])
    
    # Generate the triangle row by row
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        
        # Compute the values for the current row
        for j in range(len(triangle[i - 1]) - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        
        # End each row with 1
        row.append(1)
        
        # Append the completed row to the triangle
        triangle.append(row)
    
    return triangle
