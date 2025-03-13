"""
There is an infinite number line and Q queries. One query type is BUILD X which builds an obstacle on point X. Another query type is CHECK Y N which checks if we can build N obstacles before point Y. Need to return the answer for all the CHECK query type.
"""

import bisect

def process_queries(queries):
    obstacles = [] # Sorted list to store obstacle positions
    result = [] # List to store result of CHECK queries
    
    for query in queries:
        if query.startswith('BUILD'):
            # Extract X from BUILD X query
            x = int(query.split()[1])
            # Insert X into the sorted list
            bisect.insort(obstacles, x)
            
        elif query.startswith('CHECK'):
            # Extract Y N from the CHECK Y N query
            y, n = map(int, query.split()[1:])
            
            # Count the number of obstacles less than y
            count = bisect.bisect_left(obstacles, y)
            
            # Check if count <= n
            result.append(count <= n)
            
    return result


queries = [
    "BUILD 5",
    "BUILD 3",
    "CHECK 6 2",
    "BUILD 7",
    "CHECK 6 1",
    "CHECK 10 3"
]

result = process_queries(queries)
print(result)