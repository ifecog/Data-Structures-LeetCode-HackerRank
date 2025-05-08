"""Given a 2D matrix where each cell have value either 0 or 1, 0 means it is empty space and 1 means there is a car parked, find shortest distance to every empty space from the car."""

# BFS  finds the shortest path in an unweighted grid with minimal steps from 1 to 0. Multi-source BFS allows us to start from all 1s simultaneously, reducing redundant searches

from collections import deque

def shortestDistance(grid):
    if not grid or not grid[0]:
        return []
    
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    distance = [[-1] * n for _ in range(m)]
    
    queue = deque()
    
    # Enqueue all parked positions (1s) and mark them as distance 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                distance[i][j] = 0
                
    while queue:
        i, j, d = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and distance[ni][nj] == -1:
                distance[ni][nj] = d + 1
                queue.append((ni, nj, d + 1))
                
    return distance


grid = [
    [1, 0, 0],
    [0, 0, 1],
    [1, 0, 0]
]

print(shortestDistance(grid))


