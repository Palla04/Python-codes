def print_spiral(matrix):
    if not matrix:
        return

    # Initialize the boundaries
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=" ")
        top += 1

        # Print right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=" ")
        right -= 1

        # Print bottom row (if there is any remaining row)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        # Print left column (if there is any remaining column)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1

# Example 2D list (matrix)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Call the function
print_spiral(matrix)
