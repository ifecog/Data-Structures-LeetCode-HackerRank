import heapq

def swimInWater(grid):
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Min heap to store (max_eleveation_so_far and i, j)
    heap = [(grid[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    while heap:
        t, i, j = heapq.heappop(heap)
        if i == n - 1 and j == n - 1:
            return t

        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = True
                
                # Push the max elevation encountered so far to the heap
                heapq.heappush(heap, (max(t, grid[ni][nj]), ni, nj))
                
    return -1
                
grid = [
    [0, 2],
    [1, 3]
]
print(swimInWater(grid))                

# def findMinDifference(timePoints):
#     minutes = []
#     for time in timePoints:
#         h, m = map(int, time.split(':'))
#         minutes.append((h * 60) + m)
        
#     minutes.sort()
    
#     min_diff = float('inf')
#     for i in range(1, len(minutes)):
#         min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
#     min_diff = min(min_diff, (1440 + minutes[0]) - minutes[-1])
    
#     return min_diff

# # Test findMinDifference
# timePoints = ["23:59", "00:00", "12:34"]
# print("Minimum Time Difference:", findMinDifference(timePoints))

# from collections import defaultdict, deque

# def maximumDetonation(bombs):
#     n = len(bombs)
#     adj_list = defaultdict(list)
    
#     for i in range(n):
#         x1, y1, r = bombs[i]
        
#         for j in range(n):
#             if i != j:
#                 x2, y2, _ = bombs[j]
                
#                 if ((x2 - x1) ** 2) + ((y2 - y1) ** 2) <= r ** 2:
#                     adj_list[i].append(j)
                    
                    
#     def bfs(start):
#         visited = {start}
#         queue = deque([start])
#         count = 1
        
#         while queue:
#             node = queue.popleft()
            
#             for neighbor in adj_list[node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(neighbor)
#                     count += 1
        
#         return count
    
#     max_detonations = 0
#     for i in range(n):
#         max_detonations = max(max_detonations, bfs(i))
    
#     return max_detonations



# from collections import deque

# def swimInWater(grid):
#     n = len(grid)
#     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
#     # Binary search for the minimum t
#     left = grid[0][0]
#     right = max(max(row) for row in grid)
    
#     while left < right:
#         mid = (left + right) // 2
        
#         visited = [[False] * n for _ in range(n)]
#         visited[0][0] = True
        
#         queue = deque()
#         queue.append((0, 0))
        
#         while queue:
#             i, j = queue.popleft()
            
#             if i == n - 1 and j == n - 1:
#                 break
            
#             for di, dj in directions:
#                 ni, nj = i + di, j + dj
#                 if 0 <= ni < n and 0 <= nj < n and not grid[ni][nj] and grid[ni][nj] <= mid:
#                     grid[ni][nj] = True
#                     queue.append((ni, nj))
                    
#         # If we've reached the destination, try a smaller t
#         if visited[n - 1][n - 1]:
#             right = mid
#         else:
#             left = mid + 1
            
#     return left

# grid = [
#     [0, 2],
#     [1, 3]
# ]
# print(swimInWater(grid))