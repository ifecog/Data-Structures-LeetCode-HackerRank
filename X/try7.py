def num_islands(grid):
    # This is solved using the Depth-First-Search approach
    num_of_islands = 0
    
    def dfs(r, c):
        # If the rows and columns are out of bound, return nothing
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return
        
        # Mark the current cell as visited
        grid[r][c] = '0'
        
        # Recursively explore adjacent cells (DFS traversal)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_of_islands += 1
                dfs(i, j)
    
    return num_of_islands


# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid))