"""
305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class NumIslands2:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.parent = {}
        self.rank = {}
        self.num_islands = 0
        self.grid = [[0] * n for _ in range(m)]
        
    def _get_id(self, i, j):
        """Convert 2D coordinate to 1D id for DSU."""
        return (i * self.n) + j
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank. Only decremeent island count if roots are different."""
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return
        
        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            
        # Merge 2 separate islands
        self.num_islands -= 1
        
    def setLand(self, i, j):
        if self.grid[i][j] == 1:
            return
        
        self.grid[i][j] = 1
        idx = self._get_id(i, j)
        
        self.parent[idx] = idx
        self.rank[idx] = 0
        self.num_islands += 1
        
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < self.m and 0 <= nj < self.n and self.grid[ni][nj] == 1:
                neighbor_idx = self._get_id(ni, nj)
                self.union(idx, neighbor_idx)
                
                
    def numberOfIslands(self):
        return self.num_islands
    
obj = NumIslands2(3, 3)
obj.setLand(0, 0)
print(obj.numberOfIslands())  # 1
obj.setLand(0, 1)
print(obj.numberOfIslands())  # 1 (merged)
obj.setLand(1, 2)
print(obj.numberOfIslands())  # 2


def closedIsland(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    count = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        
        if grid[i][j] == 1:
            return True
        
        grid[i][j] = 1
        
        up = dfs(i - 1, j)
        down = dfs(i + 1, j)
        left = dfs(i, j - 1)
        right = dfs(i, j + 1)
        
        return up and down and left and right
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                if dfs(i, j):
                    count += 1
                    
    return count