def num_islands(grid):
    island_count = 0

    # Define a DFS helper function that takes in the current row and column as arguments
    def dfs(r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
            return 
        
        # Mark the current sell as visited
        grid[r][c] = '0'
        
        # Resursively explore adjacent cells
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