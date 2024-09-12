def num_islands(grid):
    """Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Args:
        grid (string): A map of '0s' and '1s'

    Returns:
        int: The numebr of islands
    """
    
    island_count = 0
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                island_count += 1

                # Traverse the island
                dfs(i, j)
    
    return island_count

# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid))