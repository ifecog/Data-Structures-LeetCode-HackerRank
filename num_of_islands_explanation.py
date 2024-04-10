    """
    Define a function numIslands(grid) that takes the 2D binary grid as input.
    
    Initialize a variable islands_count to keep track of the number of islands.
    
    Define a helper function dfs that takes the current row and column indices as arguments.
    
    In the dfs function:
    
    If the current cell is water (grid[r][c] == '0'), return.
    
    Mark the current cell as visited by changing its value to '0'.
    
    Recursively call dfs on adjacent cells (up, down, left, right) if they are within the bounds of the grid and are not visited.
    
    Iterate through each cell in the grid:

    If the current cell is land (grid[i][j] == '1'), increment islands_count and call dfs to traverse the island.

    Return the islands_count.
    """