"""You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s."""

from collections import defaultdict

def largestIsland(grid):
    if not grid:
        return 0
    
    n = len(grid)
    label = 2
    island_area = defaultdict(int)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    
    def dfs(i, j, current_label):
        if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
            return 0
        
        grid[i][j] = current_label
        area = 1
        
        for di, dj in directions:
            area += dfs(i + di, j + dj, current_label)
            
        return area

    # Step1: Label all islands and return their areas
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                area = dfs(i, j, label)
                island_area[label] = area
                label += 1
                
    max_area = max(island_area.values(), default=0)

    
    # Step 2: Check each 0 to see if flipping it can connect islands
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                neighbor = set()
                area = 1
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n:
                        island_idx = grid[ni][nj]
                        
                        if island_idx > 1 and island_idx not in neighbor:
                            neighbor.add(island_idx)
                            area += island_area[island_idx]
                            
                max_area = max(max_area, area)
                
    return max_area if max_area > 0 else n * n
  


# Example usage
grid = [[1,0],[0,1]]
print(largestIsland(grid))