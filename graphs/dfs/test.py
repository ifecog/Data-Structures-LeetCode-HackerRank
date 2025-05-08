def closedIslands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    closed_count = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        if grid[i][j] == 1:
            return True
        
        grid[i][j] = 1
        
        top = dfs(i - 1, j)
        bottom = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)
        
        return top and bottom and left and right
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                if dfs(i, j):
                    closed_count += 1
    
    return closed_count
