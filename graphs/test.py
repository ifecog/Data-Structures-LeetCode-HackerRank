from collections import defaultdict, deque


# # 2. Knight Moves
# # Possible movements for a knight
# knight_moves = [
#     (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
# ]

# def is_within_board(x, y, N):
#     return 0 <= x < N and 0 <= y < N


# def min_knight_moves(N, start, end):
#     x1, y1 = start
#     x2, y2 = end
    
#     if (x1, y1) == (x2, y2):
#         return 0
    
#     # Queue for BFS, storing (current_psition, hop_count)
#     queue = deque([(x1, y1, 0)])
    
#     # Set to keep track of the visited positions
#     visited_positions = set([x1, y1])
    
#     while queue:
#         x, y, hops = queue.popleft()
        
#         # Explore all possible knight moves
#         for dx, dy in knight_moves:
#             new_x, new_y = x + dx, y + dy
            
#             if (new_x, new_y) == (x2, y2):
#                 return hops + 1
            
#             if is_within_board(new_x, new_y, N) and (new_x, new_y) not in visited_positions:
#                 queue.append((new_x, new_y, hops + 1))
#                 visited_positions.add((new_x, new_y))
    
#     # If the target is unreachable, return -1
#     return -1

# # Example usage:
# N = 8  # Chessboard size (8x8)
# start = (0, 0)  # Starting position of the Knight
# end = (7, 7)  # Destination position
# print(min_knight_moves(N, start, end))


# 1. Bus routes
def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0
    
    # Build the graph
    stop_to_routes = defaultdict(set)
    
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
    
    # BFS
    queue = deque([(source, 0)])
    visited_stops = set([source])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        # For every bus going through the current stop, we iterate over all the stops in that route. If there is a bus stop that has not been visited, we append it to the queue and increment the number of buses taken
        for route_index in list(stop_to_routes[current_stop]):
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add((next_stop))
            
            stop_to_routes[current_stop].remove(route_index)
    
    return -1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))