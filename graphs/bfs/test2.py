# Bus Route
from collections import defaultdict, deque

def num_buses_to_destination(routes, source, target):
    # This is solved using Kahn's algorithm
    
    if source == target:
        return 0
    
    # Iniialize a set to store the stops on the routes
    stop_to_routes = defaultdict(set)
    
    # Build the graph
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
            
    # Initialize a queue for traversal and a set to keep track of visited stops
    queue = deque([(source, 0)])
    visited_stops = set([source])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        # For every bus passing through the current stop, iterate over all the stops on that route. If there is a stop that has not been visited, append it to the queue while also incrementing the buses taken
        for route_index in list(stop_to_routes[current_stop]):
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add((next_stop))
            
            # Remove the current route index to avoid revisiting
            stop_to_routes[current_stop].remove(route_index)
    
    return -1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))


# # Course Schedule
# from collections import defaultdict, deque

# def find_order(num_courses, prerequisites):
#     # This is solved using BFS
#     adj_list = defaultdict(list)
#     in_degree = [0] * num_courses
    
#     # Build the graph
#     for course, pre in prerequisites:
#         adj_list[pre].append(course)
#         in_degree[course] += 1
        
#     # Initialize a queue with all courses having an in_degree of 0 (no prerequisites)
#     queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
#     order = []
    
#     while queue:
#         course = queue.popleft()
#         order.append(course)
        
#         for neighbor in adj_list[course]:
#             in_degree[neighbor] -= 1
            
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
    
#     return order if len(order) == num_courses else []

# # Example usage
# numCourses = 2
# prerequisites = [[1, 0]]
# print(find_order(numCourses, prerequisites))  # Output: [0, 1]


# # Knight Moves
# from collections import deque

# knight_moves = [
#     (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
# ]

# def is_within_boundary(x, y, N):
#     return 0 <= x < N and 0 <= y < N


# def min_knight_moves(N, start, end):
#     x1, y1 = start
#     x2, y2 = end
    
#     if (x1, y1) == (x2, y2):
#         return 0
    
#     queue = deque([(x1, y1, 0)])
#     visited_positions = set([x1, y1])
    
#     while queue:
#         cx, cy, hops = queue.popleft()
        
#         for dx, dy in knight_moves:
#             nx, ny = cx + dx, cy + dy
            
#             if (nx, ny) == (x2, y2):
#                 return hops + 1
            
#             if is_within_boundary(nx, ny, N) and (nx, ny) not in visited_positions:
#                 queue.append((nx, ny, hops + 1))
#                 visited_positions.add((nx, ny))
    
#     return -1

# # Example usage:
# N = 8  # Chessboard size (8x8)
# start = (0, 0)  # Starting position of the Knight
# end = (7, 7)  # Destination position
# print(min_knight_moves(N, start, end))

# # Connect Islands
# from collections import deque

# # Directions in all 4 possible ways
# directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# # Function to check if the coordinates are within the boundary
# def is_valid(x, y, m, n):
#     return 0 <= x < m and 0 <= y < n


# # BFS function to find and mark all the cells in an island
# def find_island(grid, visited, x, y, island_cells):
#     visited[x][y] = True
#     island_cells.append((x, y))
#     queue = deque([(x, y)])
    
#     while queue:
#         cx, cy = queue.popleft()
        
#         # Explore all 4 directions
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
            
#             # If the current cell is within the boundary, unvisited, and is an island, add it to the queue
#             if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 island_cells.append((nx, ny))
#                 queue.append((nx, ny))
    

# # Main functin to find the shortest bridge
# def min_flips_to_connect_islands(grid):
#     m, n = len(grid), len(grid[0])
    
#     # Visited matrix to keep charge of all visited cells
#     visited = [[False] * n for _ in range(m)]
    
#     island1 = []
#     island2 = []
    
#     found_first_island = False
    
#     # 1. Find and mark the first 2 islands
#     for i in range(m):
#         for j in range(n):
#             # If the grid is an island and not visited
#             if grid[i][j] == 1 and not visited[i][j]:
#                 if found_first_island == False:
#                     find_island(grid, visited, i, j, island1)
#                     found_first_island = True
#                 else:
#                     find_island(grid, visited, i, j, island2)
#                     break
        
#         if island2:
#             break
        
#     # 2. Multi-source BFS to find the shortest bridge from all cells in the first island
#     queue = deque([(x, y, 0) for x, y in island1])
#     visited = [[False] * n for _ in range(m)]
    
#     for x, y in island1:
#         visited[x][y] = True
        
#     while queue:
#         cx, cy, distance = queue.popleft()
        
#         if (cx, cy) in island2:
#             return distance - 1
        
#         # Explore all directions
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
            
#             # If the current cell is within the boundary and unvisited, add it to the queue
#             if is_valid(nx, ny, m, n) and not visited[nx][ny]:
#                 queue.append((nx, ny, distance + 1))
#                 visited[nx][ny] = True
    
#     return -1

# # Example usage
# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0],
# ]

# print(min_flips_to_connect_islands(grid))