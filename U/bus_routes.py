from collections import defaultdict, deque

import heapq

def schedule_course(courses):
    courses.sort(key=lambda i: i[1])
    
    max_heap = []
    current_time = 0
    
    for duration, lastday in courses:
        heapq.heappush(max_heap, -duration)
        current_time += duration
        
        if current_time > lastday:
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
            
    return len(max_heap)
    
    
    # courses.sort(key=lambda i: i[1])
    
    # time, count = 0, 0
    
    # for duration, lastday in courses:
    #     if time + duration <= lastday:
    #         time += duration
    #         count += 1
            
    # return count




# def num_buses_to_destination(routes, source, target):
#     if source == target:
#         return 0
    
#     routes = [set(route) for route in routes]
    
#     stop_to_routes = defaultdict(set)
#     for i, route in enumerate(routes):
#         for stop in route:
#             stop_to_routes[stop].add(i)
            
#     queue = deque([(source, 0)])
#     visited_stops = {source} # set([source])
#     visited_routes = set()
    
#     while queue:
#         current_stop, buses_taken = queue.popleft()
        
#         if current_stop == target:
#             return buses_taken
        
#         for route_index in stop_to_routes[current_stop]:
#             if route_index in visited_routes:
#                 continue
            
#             visited_routes.add(route_index)
            
#             for next_stop in routes[route_index]:
#                 if next_stop not in visited_stops:
#                     visited_stops.add((next_stop))
#                     queue.append((next_stop, buses_taken + 1))
    
#     return -1

# # Example usage:
# routes1 = [[1,2,7],[3,6,7]]
# source1 = 1
# target1 = 6
# print(num_buses_to_destination(routes1, source1, target1))