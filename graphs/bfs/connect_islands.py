from collections import deque

"""You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

    An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

    You may change 0's to 1's to connect the two islands to form one island.

    Return the smallest number of 0's you must flip to connect the two islands.

    Args:
        grid (int): N X N Matrix

    Returns:
        int:  Smallest number of 0's you must flip to connect the two islands.
"""

# Directions for moving in the matrix: right, left, up, down
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

# Function to check if the coordinates are within the boundary
def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


# BFS function to find and mark all the cells in an island
def find_island(grid, visited, x, y, island_cells):
    visited[x][y] = True
    island_cells.append((x, y))
    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # If the current cell is within the boundary, unvisited, and is an Island, add it to the queue
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                island_cells.append((nx, ny))
                queue.append((nx, ny))
                

# Main function to find the shortest bridge: minimum flips of 0s and 1s 
def min_flips_to_connect_islands(grid):   
    m, n = len(grid), len(grid[0])
    
    # Visited matrix to keep track of visited cells
    visited = [[False] * n for _ in range(m)]
    
    # Islands
    island1 = []
    island2 = []
    
    find_first_island = False
    
    # 1. Find and mark the 2 islands
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                if not find_first_island:
                    find_island(grid, visited, i, j, island1)
                    find_first_island = True
                else:
                    find_island(grid, visited, i, j, island2)
                    break
        
        if island2:
            break

    # 2. Multi-source BFS to find the shortest bridge from all cells in the first island
    queue = deque([(x, y, 0) for x, y in island1])
    visited = [[False] * n for _ in range(m)]
    
    for x, y in island1:
        visited[x][y] = True
        
    while queue:
        x, y, distance = queue.popleft()
        
        if (x, y) in island2:
            return distance - 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # If the current cell is within the boundary and unvisited, add it to the queue
            if is_valid(nx, ny, m, n) and not visited[nx][ny]:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
    
    return -1
            
    

# Example usage
grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(min_flips_to_connect_islands(grid))