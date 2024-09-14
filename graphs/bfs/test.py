from collections import defaultdict, deque

# # 3. Shortest Bridge

# # Directions for moving in the matrix: right, left, down, up
# directions = [
#     (0, 1), (0, -1), (1, 0), (-1, 0)
# ]

# # Function to check of the coordinates are within the boundaries of the matrix
# def is_valid(x, y, m, n):
#     return 0 <= x < m and 0 <= y < n


# # BFS function to find and mark all cells of an island
# def find_island(grid, visited, x, y, island_cells):
#     visited[x][y] = True
#     island_cells.append((x, y))
#     queue = deque([(x, y)])
    
#     while queue:
#         # Get the current cell
#         cx, cy = queue.popleft()
        
#         # Check al 4 directions for connected land cells
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
            
#             # If the current cell is within the boundary, unvisited, and is land, add it to the island
#             if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 island_cells.append((nx, ny))
#                 queue.append((nx, ny))


# # Main function to find the shortest brigde: minimum flips of 0s and 1s to connect 2 islands
# def shortest_bridge(grid):
#     m, n = len(grid), len(grid[0])
    
#     # Create a visited matrix to keep track of visited cells
#     visited = [[False] * n for _ in range(m)]
    
#     island1 = []
#     island2 = []
    
#     found_first_island = False
    
#     # 1. Find and mark the 2 islands
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == 1 and not visited[i][j]:
#                 if not found_first_island:
#                     # Find the first island
#                     find_island(grid, visited, i, j, island1)
#                     found_first_island = True
#                 else:
#                     # If the first island has already been found, this must be the 2nd island
#                     find_island(grid, visited, i, j, island2)
#                     break
                
#         if island2:
#             break
        
#     # 2. Multi-source BFS to find the shortest bridge from all cells in the first island
#     queue = deque([(x, y, 0) for x, y in island1])
#     visited = [[False] * n for _ in range(m)]
    
#     for x, y, in island1:
#         visited[x][y] = True
        
#     while queue:
#         x, y, distance = queue.popleft()
        
#         # If we've reached an cell in the second island, return the distance
#         if (x, y) in island2:
#             return distance - 1
        
#         # Explore all 4 directions
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
            
#             # If the new cell is within the bounds and unvisited, add it to the queue
#             if is_valid(nx, ny, m, n) and not visited[nx][ny]:
#                 queue.append((nx, ny, distance + 1))
#                 visited[nx][ny] = True
    
#     return -1


# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0],
# ]

# print(shortest_bridge(grid))  # Output should be 1


# # 2. Minimum knight moves
# directions = [
#     (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
# ]

# def is_valid(x, y, N):
#     return 0 <= x < N and 0 <= y < N


# def min_knight_moves(N, start, end):
#     x1, y1 = start
#     x2, y2 = end
    
#     if (x1, y1) == (x2, y2):
#         return 0
    
#     # BFS
#     visited_positions = set([x1, y1])
#     queue = deque([(x1, y1, 0)])
    
#     while queue:
#         x, y, hops = queue.popleft()
        
#         # Explore all 8 knoght moves
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
            
#             if (nx, ny) == (x2, y2):
#                 return hops + 1
            
#             # If the cell is within the boundary and unvisited, add it to the queue
#             if is_valid(nx, ny, N) and (nx, ny) not in visited_positions:
#                 queue.append((nx, ny, hops + 1))
#                 visited_positions.add((nx, ny))
        
#     return -1


# # Example usage:
# N = 8  # Chessboard size (8x8)
# start = (0, 0)  # Starting position of the Knight
# end = (7, 7)  # Destination position
# print(min_knight_moves(N, start, end))


# # 1. Bus Routes
# def num_buses_to_destination(routes, source, target):
#     if source == target:
#         return 0
    
#     # Build the graph stop_to_routes
#     stop_to_routes = defaultdict(set)
    
#     for i, route in enumerate(routes):
#         for stop in route:
#             stop_to_routes[stop].add(i)
            
#     # BFS
#     visited_stops = set([source])
#     queue = deque([(source, 0)])
    
#     while queue:
#         current_stop, buses_taken = queue.popleft()
        
#         if current_stop == target:
#             return buses_taken
        
#         # For every bus passing through the current stop, we iterate over all te stops on that route. If there is a bus stop (next stop) that has not been visited, we add it to the queue.
        
#         for route_index in list(stop_to_routes[current_stop]):
#             for next_stop in routes[route_index]:
#                 if next_stop not in visited_stops:
#                     queue.append((next_stop, buses_taken + 1))
#                     visited_stops.add((next_stop))
            
#             stop_to_routes[current_stop].remove(route_index)
    
#     return -1

# # Example usage:
# routes1 = [[1,2,7],[3,6,7]]
# source1 = 1
# target1 = 6
# print(num_buses_to_destination(routes1, source1, target1))