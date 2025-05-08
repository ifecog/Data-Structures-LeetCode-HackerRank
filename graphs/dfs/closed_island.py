"""Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands."""


def closedIsland(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        
        if grid[i][j] == 1:
            return True
        
        grid[i][j] = 1
        
        up = dfs(i - 1, j)
        down = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)
        
        return up and down and left and right
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                if dfs(i, j):
                    count += 1
    
    return count

# Example usage
grid = [
    [1,1,1,1,1,1,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,1,0,1,1,1,0],
    [1,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0]
]

print(closedIsland(grid))