from collections import deque


# Directions for moving in the matrix: right, left, up, down
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

# Function to check if the coordinates are within the boundary
def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


# BFS function to find and mark all cells of an island
def find_island(grid, visited, x, y, island_cells):
    queue = deque([(x, y)])
    visited[x][y] = True
    island_cells.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # If the current cell is within the boundary, unvisited, and is an island, add it to the island
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                island_cells.append((nx, ny))
                queue.append((nx, ny))
                

# Main function to find the shortest bridge: minimum flips of 0s and 1s 
def min_flips_to_connect_islands(grid):
    """You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

    An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

    Args:
        grid (int): N X N Matrix

    Returns:
        int:  Smallest number of 0's you must flip to connect the two islands.
    """
    m, n = len(grid), len(grid[0])
    
    # Create a visited matrix to keep track of visited cells
    visited = [[False] * n for _ in range(m)]
    
    island1 = []
    island2 = []
    
    found_first_island = False 
    
    # 1. Find and mark the 2 islands
    for i in range(m):
        for j in range(n):
            # If the current grid is an island and unvisited
            if grid[i][j] == 1 and not visited[i][j]:
                if not found_first_island:
                    # Mark all cells of the first island
                    find_island(grid, visited, i, j, island1)
                    found_first_island = True
                else:
                    # If the first island has already been found, this must be the second island
                    # Mark all cells of the second island
                    find_island(grid, visited, i, j, island2)
                    break
                    
        if island2:
            break
    
    # 2. Multi-source BFS from all cells in the first island
    queue = deque([(x, y, 0) for x, y in island1])
    visited = [[False] * n for _ in range(m)]
    
    for x, y in island1:
        visited[x][y] = True
        
    while queue:
        x, y, distance = queue.popleft()

        # If we've reached any cell in the second island, return the distance
        if (x, y) in island2:
            return distance - 1
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # If the new cell is within the boundary and unvisited, add it to the queue
            if is_valid(nx, ny, m, n) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
                
    return -1


# Example usage
grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(min_flips_to_connect_islands(grid))