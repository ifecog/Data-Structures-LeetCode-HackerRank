"""You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points."""

import heapq

def minCostConnectPoints(points):
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)] # (cost, point_index)
    total_cost = 0
    
    while min_heap:
        cost, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        total_cost += cost
        
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (dist, v))
                
    return total_cost

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points))


# # Kruskal'ss algorithm
# class DSU:
#     def __init__(self, n):
#         self.parent = list(range(n))
#         self.rank = [0] * n
        
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
        
#         return self.parent[x]
    
#     def union(self, x, y):
#         rootX, rootY = self.find(x), self.find(y)
#         if rootX == rootY:
#             return False
        
#         if self.rank[rootX] < self.rank[rootY]:
#             self.parent[rootX] = rootY
#         elif self.rank[rootY] < self.rank[rootX]:
#             self.parent[rootY] = rootX
#         else:
#             self.parent[rootY] = rootX
#             self.rank[rootX] += 1
        
#         return True
    
# def minCostConnectPoints(points):
#     n = len(points)
#     edges = []
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             xi, yi = points[i]
#             xj, yj = points[j]
#             dist = abs(xi - xj) + abs(yi - yj)
#             edges.append((dist, i, j))
    
#     edges.sort()
    
#     dsu = DSU(n)
#     mst_cost = 0
#     edges_used = 0
    
#     for cost, u, v in edges:
#         if dsu.union(u, v):
#             mst_cost += cost
#             edges_used += 1
            
#             if edges_used == n - 1:
#                 break
    
#     return mst_cost

# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# print(minCostConnectPoints(points))

