import heapq

def swimInWater(grid):
    n = len(grid)
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Min heap to store (max-elevation-so-far and i, j)
    heap = [(grid[0][0], 0, 0)]
    print(heap)
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while heap:
        t, i, j = heapq.heappop(heap)
        
        if i == n - 1 and j == n - 1:
            return t
        
        # Explore neighbors
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                
                # Push the maximum elevation encountered so far
                heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))
    
    return -1


grid = [
    [0, 2],
    [1, 3]
]
print(swimInWater(grid))