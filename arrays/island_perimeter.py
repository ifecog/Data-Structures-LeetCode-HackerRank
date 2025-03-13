def islandPerimeter(grid):
    """
    You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

    Args:
        grid (int): a row x col grid
    """
    
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            # Initially add 4 to every land cell encountered
            if grid[i][j] == 1:
                perimeter += 4
                
                # Remove 2 if there's land to the top
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                
                # Remove 2 if there's land to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                
    return perimeter

# Example usage
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))