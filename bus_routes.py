from collections import defaultdict, deque

def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0
    
    # Build a graph where each bus stop is a key and its connected bus stops are the values
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    # Initialize a set to keep track of visited bus stops and a queue for BFS traversal
    visited_stops = set([source])
    queue = deque([(source, 0)])
    
    # perform BFS
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        # check if current stop is the target
        if current_stop == target:
            return 
        
        # Iterate over all buses passing through the current stop
        for route_index in list(stop_to_routes[current_stop]):
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add(next_stop)
                    
            # Remove the route from the dictionary to avoid reveisiting
            del routes[route_index]
    
    # If the target bus stop is not reachable
    return - 1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))  # Output: 2

routes2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source2 = 15
target2 = 12
print(num_buses_to_destination(routes2, source2, target2))  # Output: -1

