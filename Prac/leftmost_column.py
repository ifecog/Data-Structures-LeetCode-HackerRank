def leftmost_column_with_one(binaryMatrix):
    """A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

    Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

    Args:
        binaryMatrix (int): a 2 x 2 matrix of 0s and 1s
        
    Solution:
    
    Start from the top-right corner of the matrix
    
    Initialize the leftmost column to -1
    
    Iterate through each row:
        if the current cell contains '1', move left to explore further for the leftmost '1' column
        
        Fit the current cell contains '0', move down to the next row (we can't find any 1 to the right)
    
    """
    if  not binaryMatrix or not binaryMatrix[0]:
        return -1
    
    row, col = 0, len(binaryMatrix[0]) - 1
    
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