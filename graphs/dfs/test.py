from collections import deque

# 2. Shortest Bridge

directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


def find_island(grid, visited, x, y, island_cells):
    visited[x][y] = True
    island_cells.append((x, y))
    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                island_cells.append((nx, ny))
                queue.append((nx, ny))
                

def shortest_bridge(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    island1 = []
    island2 = []
    found_first_island = False
    
    # 1. Find and mark the 2 islands
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                if not found_first_island:
                    # Mark all cells of the first island
                    find_island(grid, visited, i, j, island1)
                    found_first_island = True
                else:
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
        x, y, dist = queue.popleft()
        
        
        # If we've reached any cell in the second island, return the distance
        if (x, y) in island2:
            return dist - 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny, m, n) and not visited[nx][ny]:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True
    
    return -1

# Example usage
grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(shortest_bridge(grid))