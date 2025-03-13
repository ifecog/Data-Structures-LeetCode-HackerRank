def generateMatrix(n):
    """
    Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

    Args:
        n (n): A positive integer to fill in the matrix
    """
    
    matrix = [[0] * n for _ in range(n)]
    
    top = left = 0
    bottom = right = n - 1
    
    num = 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            
    return matrix


# Example usage
n = 3
print(generateMatrix(n))