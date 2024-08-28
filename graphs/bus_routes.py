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
    
    # 1. Build the graphh
    
    # Initialize a set tp store the stops on the routes using a dictionary stop_to_routes
    stop_to_routes = defaultdict(set)
    
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    # 2. BFS. 
    
    # Initialize a queue for traversal and a set to keep track of visited stops
    queue = deque([(source, 0)])
    visited_stops = set([source])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        # For every bus passing through the current stop, we iterate over all the stops on that route. If there is a bus stop that has not been visited, we append it to the queue while also incrementing the buses taken.
        for route_index in list(stop_to_routes[current_stop]):
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add((next_stop))
            
            # The current route index is removed to avoid revisiting
    
    return -1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))