def num_islands(grid):
    """Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Args:
        grid (string): A map of '0s' and '1s'

    Returns:
        int: The numebr of islands
    """
    
    islands_count = 0
    
    # Define helper function that takes the current row and column indices as arguments
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        # Mark current cell as visited
        grid[row][col] = '0'
        
        # Recursively explore adjacent cells
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands_count += 1
                
                # Traverse the island
                dfs(i, j)
    
    return islands_count
    
    
# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid))