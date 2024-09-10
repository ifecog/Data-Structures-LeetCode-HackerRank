from collections import deque

# Shortest Bridge

# Directions for moving in the matrix: right, left, down, up
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

# Function to check of the coordinates are within the boundaries of the matrix
def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


# BFS function to find and mark all cells of an island
def find_island(grid, visited, x, y, island_cells):
    visited[x][y] = True
    island_cells.append((x, y))
    queue = deque([(x, y)])
    
    while queue:
        # Get the current cell
        cx, cy = queue.popleft()
        
        # Check al 4 directions for connected land cells
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            # If the current cell is within the boundary, unvisited, and is land, add it to the island
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                island_cells.append((nx, ny))
                queue.append((nx, ny))


# Main function to find the shortest brigde: minimum flips of 0s and 1s to connect 2 islands
def shortest_bridge(grid):
    m, n = len(grid), len(grid[0])
    
    # Create a visited matrix to keep track of visited cells
    visited = [[False] * n for _ in range(m)]
    
    island1 = []
    island2 = []
    
    found_first_island = False
    
    # 1. Find and mark the 2 islands
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                if not found_first_island:
                    # Find the first island
                    find_island(grid, visited, i, j, island1)
                    found_first_island = True
                else:
                    # If the first island has already been found, this must be the 2nd island
                    find_island(grid, visited, i, j, island2)
                    break
                
        if island2:
            break
        
    # 2. Multi-source BFS to find the shortest bridge from all cells in the first island
    queue = deque([(x, y, 0) for x, y in island1])
    visited = [[False] * n for _ in range(m)]
    
    for x, y, in island1:
        visited[x][y] = True
        
    while queue:
        x, y, distance = queue.popleft()
        
        # If we've reached an cell in the second island, return the distance
        if (x, y) in island2:
            return distance - 1
        
        # Explore all 4 directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # If the new cell is within the bounds and unvisited, add it to the queue
            if is_valid(nx, ny, m, n) and not visited[nx][ny]:
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = True
    
    return -1


grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(shortest_bridge(grid))  # Output should be 1
