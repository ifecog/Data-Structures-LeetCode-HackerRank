from collections import deque

def shortest_bridge(grid):
    n = len(grid)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def dfs(i, j, island):
        if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
            return
        
        grid[i][j] = island
        
        for di, dj in directions:
            dfs(i + di, j + dj, island)
            
    island = 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, island)
                island += 1
                
    queue = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
                
    while  queue:
        i, j, flips = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj 
            
            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 3:
                    return flips
                
                if grid[ni][nj] == 0:
                    grid[ni][nj] == 2
                    queue.append((ni, nj, flips + 1))
                    
    return -1
            

grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(shortest_bridge(grid))
            
            
def orangesRottling(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    fresh_orranges = 0
    
    queue = deque()
    for i in range(m):
        for j  in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            
            elif grid[i][j] == 1:
                fresh_orranges += 1
                
    minutes_elapsed = 0
    while queue:
        i, j, minutes = queue.popleft()
        minutes_elapsed = max(minutes_elapsed, minutes)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh_orranges -= 1
                queue.append((ni, nj, minutes + 1))
                
    return minutes_elapsed if fresh_orranges == 0 else 1

# Example usage
# grid1 = [
#     [2, 1, 1],
#     [1, 1, 0],
#     [0, 1, 1]
# ]

# print(orangesRottling(grid1))