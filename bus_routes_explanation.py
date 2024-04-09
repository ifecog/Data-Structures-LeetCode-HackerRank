    # """
    # Solution:
    # This is solved using the BFS algorithm
    
    # Import the defaultdict and the deque class from the collections module. The deque class is a queue data structure in the BFS algorithm.
    
    # The bfs function (num_buses_to_destination) is defined. This takes in 3 parameters:
    #     routes - a graph in the form of an adjacency list
    #     source - the starting vertex for BFS traversal
    #     target = the value being searched for in the graph
        
    # If the source parameter is equal to the target, return 0, implying that no buses have to be taken from source to target
    
    # 1. Build the graph    
    # Use a dictionary 'stop_to_routes' to build the graph.
    
    # note: each bus stop is a node/vertex and each bus route is an edge connecting the bus stops.
        
    # Each bus stop is a key and its connected bus stops are the values.
     
    # 2. Perform BFS
    # Initialize a set to keep track of visited bus stops and a queue for BFS traversal.
    
    # Create a while loop that continues until the queue becomes empty indicating that all vertices have been visited or that the target has been found.
    
    # Create a variable 'current_stop' that continuously get popped to arraive at the target. If current stop is equal to the target, return buses taken.
    
    # 3. Exploring Neighbors:
    # During BFS traversal, for each bus stop (current_stop) popped from the queue, we examine all buses passing through that stop. 
    
    # Note: modifying a set during iteration is not allowed in Python and would result in a runtime eror. So, a copy of the set is created before iterating ovet it.
    
    # For each bus route passing through current_stop, we iterate over all the stops on that route.
    
    # If we encounter a bus stop (next_stop) that we haven't visited before, we add it to the queue along with the number of buses taken to reach it (buses_taken + 1). We also mark it as visited.
    
    # """

from collections import defaultdict, deque


def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0
    
    # Build graph 
    
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    # BFS
    
    visited_routes = set([source])
    queue = deque([(source, 0)])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        if current_stop == target:
            return buses_taken
        
        # make a copy of the set for the purpose of iteration
        routes_for_current_stop = stop_to_routes[current_stop].copy()
        # iterate over buses passing through the route
        for route_index in routes_for_current_stop:
            for next_stop in routes[route_index]:
                if next_stop not in visited_routes:
                    queue.append((next_stop, buses_taken + 1))
                    visited_routes.add(next_stop)
            
            # remove the current stop from the set to avoid revisiting
            stop_to_routes[current_stop].remove(route_index)
    
    return -1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))  # Output: 2
