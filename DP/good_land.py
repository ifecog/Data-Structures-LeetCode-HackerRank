# dp[i][j] is the size of the largest square whose bottom-right corner is at cell (i, j)
# if matrix[i][j] = 1; dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

def maxGoodLandArea(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    
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
                    
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side
    
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
print(maxGoodLandArea(matrix))