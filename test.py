from collections import defaultdict, deque

def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0
    
    # 1. Build the graph
    
    # Iitialize to set to store the stops on the routes
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    
    # 2. BFS
    
    # Initialize a set to keep track of te visited stops and a queue for BFS traversal
    visited_stops = set([source])
    queue = deque([(source, 0)])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        # 3. Explore neighbors
        
        # Create a copy of the stop_to_routes set for the purpose of iteration (modifying a set during iteration in Python would result in a runtime error)
        current_stop_to_routes = stop_to_routes[current_stop].copy()
        
        # a. For each bus passing through the current stop, we iterate over all stops on that route.
        # b. If we encounter a bus stop (next stop) thaat has not been visited, we append it to the queue, whlie incrementing the num_buses taken by 1. Also, we mark it as visited by adding it to the visited_stops.
        
        for route_index in current_stop_to_routes:
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add(next_stop)
            
            # we remove the current stop to avoid revisiting
            stop_to_routes[current_stop].remove(route_index) 
    
    
    return -1   
            

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))  # Output: 2

routes2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source2 = 15
target2 = 12
print(num_buses_to_destination(routes2, source2, target2))  # Output: -1
