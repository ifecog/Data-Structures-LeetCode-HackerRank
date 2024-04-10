def num_islands(grid):
    islands_count = 0
    
    # Define helper function that takes the current row and column indics as arguments
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        # Mark current cell as visited
        grid[row][col] = '0'
        
        # Explore adjacent cells
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