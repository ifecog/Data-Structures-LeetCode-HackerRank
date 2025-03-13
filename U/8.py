"""
Given a matrix of size n*m with tower heights as input. For each tower you are allowed to jump to other neighbour tower if height of current tower < height of neighbour tower. Find the maximum number of towers you can jump.
"""

def maxTowerJumps(matrix):
    if not matrix and not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    
    dp = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        
        max_jumps = 0
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                max_jumps = max(max_jumps, dfs(ni, nj))
                
        dp[i][j] = 1 + max_jumps
        
        return dp[i][j]
    
    max_no_of_towers = 0
    for i in range(m):
        for j in range(n):
            max_no_of_towers = max(max_no_of_towers, dfs(i, j))
            
    return max_no_of_towers


# Example usage
matrix = [
    [60, 60, 40],
    [50, 40, 45],
    [15, 10, 10]
]
print(maxTowerJumps(matrix))