"""A farmer wants to farm their land with the maximum area where good land is present. The land is represented as a matrix with 1s and 0s. 1s mean good land and 0s means bad land. The farmer wants to  farm in a square of good land with the maximum area. Please, help the farmer to find the maximum area of the land they can farm in good land."""

# dp[i][j] is the size of the largest square whose bottom-right corner is at cell (i, j)
# if matrix[i][j] == 1:
# dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

def maxGoodLandArea(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    
    dp = [[0] * n for _ in range(m)]
    max_size = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1
                
                max_size = max(max_size, dp[i][j])
    
    return max_size * max_size


matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(f'Area = {maxGoodLandArea(matrix)}m2')  # Output: 9 (3x3 square)
