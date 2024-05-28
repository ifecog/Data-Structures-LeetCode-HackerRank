from collections import defaultdict, deque


def num_buses_to_destination(routes, source, target):
    """
    You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
    You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

    Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

    Args:
        routes (graph): a graph in the form of an adjacency list
        source (int): starting vertex for the BFS traversal
        target (int): the value being searched for in the graph
        
    Returns:
        int: the least number of buses
    """
    
    if source == target:
        return 0
    
    # 1. Build the graph
    
    # Initialize a set to store the stops on the routes using a dictionary stop_to_routes
    stop_to_routes = defaultdict(set)
    
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    # 2. BFS
    
    # Initialize a set to store the visited stops and a queue for BFS traversal
    visited_stops = set([source])
    queue = deque([(source, 0)])
    
    while queue:
        # Initialize the current stop
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        # For each bus passing through the current stop, we iterate over all stops on that route. If there is a bus stop (next stop) that has not been visited, we append it to the queue while also incrementing the buses taken by 1. Also, we add it to the visited stops.
        
        # We create a copy of the stop_to_routes for the purpose of iteration. This is because making changes to a set during iteration on Python would result in a runtime error.
        # current_stop_to_routes = stop_to_routes[current_stop].copy()
        
        # for route_index in current_stop_to_routes:
        for route_index in list(stop_to_routes[current_stop]):
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add(next_stop)
            
            # After checking, the current route index is removed to avoid revisiting
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
