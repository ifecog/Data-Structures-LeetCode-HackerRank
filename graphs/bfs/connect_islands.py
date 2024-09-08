from collections import deque


# Directions for moving in the matrix: right, left, up, down
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


def find_island(grid, visited, x, y, island_cells):
    queue = deque([(x, y)])
    visited[x][y] = True
    island_cells.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] == True
                island_cells.append((nx, ny))
                queue.append((nx, ny))
                
                
    