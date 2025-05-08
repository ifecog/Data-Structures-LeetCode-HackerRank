from collections import deque

def orangesRotting(grid):
    """
    You are given an m x n grid where each cell can have one of three values.
    0 -> An empty cell.
    1 -> A fresh orange.
    2 -> A rotten orange.

    Args:
        grid (int): A grid of oranges
    """
    
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    fresh_oranges = 0
    
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
                
            elif grid[i][j] == 1:
                fresh_oranges += 1
                
    minutes_elapsed = 0
    while queue:
        i, j, minutes = queue.popleft()
        minutes_elapsed = max(minutes_elapsed, minutes)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh_oranges -= 1
                queue.append((ni, nj, minutes + 1))
                
    return minutes_elapsed if fresh_oranges == 0 else -1
    

# Example usage
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(orangesRotting(grid1))
                
    