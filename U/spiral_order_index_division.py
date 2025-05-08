"""
Flatten the matrix by spiral iteration and output the sum of elements whose index is divisible by 3.
"""

def spiral_order(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse form right to left along the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        # Traverse from bottom to top along the left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result
        
        
def sum_divisible_by_3(matrix):
    flattened = spiral_order(matrix)
    total = 0
    
    for i in range(len(flattened)):
        if i % 3 == 0:
            total += flattened[i]
    
    return total

# # Example usage
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(spiral_order(matrix))   
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_divisible_by_3(matrix)
print(result)