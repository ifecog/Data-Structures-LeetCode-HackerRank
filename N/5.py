def leftmost_column_with_one(binaryMatrix):
    row, col = 0, len(binaryMatrix) - 1
    
    leftmost_col = -1
    
    while row < len(binaryMatrix) and col >= 0:
        if binaryMatrix[row][col] == 1:
            leftmost_col = col
            col -= 1
        else:
            row += 1 
    
    return leftmost_col

# Example usage:
binaryMatrix = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 0]
]

print(leftmost_column_with_one(binaryMatrix)) 