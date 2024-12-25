# Course Schedule 2
from collections import defaultdict, deque

def find_order(num_courses, prerequisites):
    # Store the graph as an adjacency list
    adj_list = defaultdict(list)
    
    # In_degree array to store how many prerequisite each course has
    in_degree = [0] * num_courses
    
    for course, pre in prerequisites:
        adj_list[pre].append(course)
        in_degree[course] += 1
        
    # Initiate a queue with all courses having an in_degree of 0 (i.e. no prerequisites)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
    # Empty list to store final ordering
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return True if len(order) == num_courses else False

# Example usage
numCourses = 2
prerequisites = [[1, 0]]
print(find_order(numCourses, prerequisites))  # Output: [0, 1]


# # Course Schedule 1
# from collections import defaultdict, deque

# def find_order(num_courses, prerequisites):
#     # Store the graph as an adjacency list
#     adj_list = defaultdict(list)
    
#     # In-degree array to store how many prerequisites each course has
#     in_degree = [0] * num_courses
    
#     for course, pre in prerequisites:
#         adj_list[pre].append(course)
#         in_degree[course] += 1
        
#     # Initialize a queue with all courses having an in_degree of 0 (meaning no prerequisites)
#     queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
#     # Empty list to store the final course ordering
#     order = []
    
#     while queue:
#         course = queue.popleft()
#         order.append(course)
        
#         # Process each neighbor and reduce the in_degree
#         for neighbor in adj_list[course]:
#             in_degree[neighbor] -= 1
            
#             # If the dependent course (the neighbor) has no prerequisites, add it to the queue
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
                
#     return order if len(order) == num_courses else []

# # Example usage
# numCourses = 2
# prerequisites = [[1, 0]]
# print(find_order(numCourses, prerequisites))
    

# # Connect Islands
# from collections import deque

# directions = [
#     (0, 1), (0, -1), (1, 0), (-1, 0)
# ]

# # Check if the coordinates are within the boundary
# def is_valid(x, y, m, n):
#     return 0 <= x < m and 0 <= y < n


# # BFS function to find and mark all the cells in an island
# def find_island(grid, visited, x, y, island):
#     visited[x][y] = True
#     island.append((x, y))
#     queue = deque([(x, y)])
    
#     while queue:
#         cx, cy = queue.popleft()
        
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
            
#             # If the current cell is withoni the boundary, unvisited, and is an island, add it to the queue
#             if is_valid(nx, ny, len(grid), len(grid[0])) and not visited[nx][ny] and grid[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 island.append((nx, ny))
#                 queue.append((nx, ny))
                

# # Main function to find the shortest brisgeL minimum flips of 0s to 1s
# def min_flips_to_connect_islands(grid):
#     m, n = len(grid), len(grid[0])
    
#     # Visited matrix to keep track of visited cells
#     visited = [[False] * n for _ in range(m)]
    
#     # Initiate islands
#     island1 = []
#     island2 = []
    
#     find_first_island = False
    
#     # 1. Find and mark the 2 islands
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == 1 and not visited[i][j]:
#                 if not find_first_island:
#                     find_island(grid, visited, i, j, island1)
#                     find_first_island = True
#                 else:
#                     find_island(grid, visited, i, j, island2)
#                     break
        
#         if island2:
#             break
        
#     # 2. Multi-source BFS to find the shortest bridge
#     queue = deque([(x, y, 0) for x, y in island1])
#     visited = [[False] * n for _ in range(m)]
    
#     for (x, y) in island1:
#         visited[x][y] = True
    
#     while queue:
#         cx, cy, distance = queue.popleft()
        
#         if (cx, cy) in island2:
#             return distance - 1
        
#         for dx, dy in directions:
#             nx, ny = cx + dx, cy + dy
            
#             # Check if the current cell is within the boundary and unvisited
#             if is_valid(nx, ny, m, n) and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny, distance + 1))
                
#     return -1

# # Example usage
# grid = [
#     [1, 1, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0],
# ]

# print(min_flips_to_connect_islands(grid))

# # Bus Routes
# from collections import defaultdict, deque

# def num_buses_to_destination(routes, source, target):
#     if source == target:
#         return 0
    
#     # Convert each route to a set for lookup purpose
#     routes = [set(route) for route in routes]
    
#     # Build the graph of stop to routes
#     stop_to_routes = defaultdict(set)
#     for i, route in enumerate(routes):
#         for stop in route:
#             stop_to_routes[stop].add(i)
            
#     # Implement Kahn's Algorithm (queue for node traversal, and sets to keep track of visited stops and visited routes)
#     queue = deque([(source, 0)])
#     visited_stops = {source}
#     visited_routes = set()
    
#     while queue:
#         current_stop, buses_taken = queue.popleft()
#         if current_stop == target:
#             return buses_taken
        
#         # Check all routes that contain the current stop 
#         for route_index in stop_to_routes[current_stop]:
#             if route_index in visited_routes:
#                 continue
#             # Add this route to the visited routes
#             visited_routes.add(route_index)
            
#             # Add all stops on this route to the visited stops
#             for next_stop in routes[route_index]:
#                 if next_stop not in visited_stops:
#                     visited_stops.add(next_stop)
#                     queue.append((next_stop, buses_taken + 1))
    
#     return -1

# # Example usage:
# routes1 = [[1,2,7],[3,6,7]]
# source1 = 1
# target1 = 6
# print(num_buses_to_destination(routes1, source1, target1))


# # Knight Moves
# from collections import deque

# # Possible moves for a knight
# coortinates = [
#     (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
# ]

# # Function to check if the coordinates are within the boundary
# def is_within_board(x, y, N):
#     return 0 <= x < N and 0 <= y < N


# def min_knight_moves(N, start, end):
#     (x1, y1) = start
#     (x2, y2) = end
    
#     if (x1, y1) == (x2, y2):
#         return 0
    
#     # Implement Kahn's Algorithm
#     queue = deque([(x1, y1, 0)])
#     visited_positions = {x1, y1}
    
#     while queue:
#         x, y, hops = queue.popleft()
        
#         # Explore the coordinates
#         for dx, dy in coortinates:
#             nx, ny = x + dx, y + dy
            
#             if (nx, ny) == (x2, y2):
#                 return hops + 1
            
#             # If the cell is within the boundary and unvisited, add it to the visited positions
#             if is_within_board(nx, ny, N) and (nx, ny) not in visited_positions:
#                 visited_positions.add((nx, ny))
#                 queue.append((nx, ny, hops + 1))        
    
#     # If the target is unreachable (which shouldn't happen on a chess board), return -1
#     return -1

# # Example usage:
# N = 8  # Chessboard size (8x8)
# start = (0, 0)  # Starting position of the Knight
# end = (7, 7)  # Destination position
# print(min_knight_moves(N, start, end))

