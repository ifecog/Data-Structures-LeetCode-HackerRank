from collections import deque

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0)
    ]
    
    # Initialize visited array with infinity
    visited = [[float('inf')] * n for _ in range(m)]
    visited[0][0] = 0
    
    queue = deque([(0, 0, 0, 0)])
    
    while queue:
        i, j, steps, obstacles = queue.popleft()
        
        # If we've reached the destination, return the number of steps
        if i == m - 1 and j == n - 1:
            return steps
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n:
                new_obstacles = obstacles + grid[ni][nj]
                
                # If the new state is better (fewer obstacles eliminated), proceed
                if new_obstacles <= k and new_obstacles < visited[ni][nj]:
                    visited[ni][nj] = new_obstacles
                    queue.append((ni, nj, steps + 1, new_obstacles))
                    
    return -1

# Example usage
grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
print(shortestPath(grid, k))