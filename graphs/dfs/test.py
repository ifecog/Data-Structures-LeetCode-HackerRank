# Calculate Equation
from collections import defaultdict

def calc_equation(equations, values, queries):
    # Build the graph
    graph = defaultdict(dict)
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1/value
        
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        
        if start == end:
            return 1.0
        
        # Mark the start node as visited
        visited.add(start)
        
        # Explore all neighbors of the start node
        for neighbor in graph[start]:
            if neighbor in visited:
                continue
            
            # Recursively explore the neighbor node
            temp = dfs(neighbor, end, visited)
            if temp != -1.0:
                return temp * graph[start][neighbor]
        
        return -1.0
    
    return [dfs(c, d, set()) if c in graph and d in graph else -1.0 for c, d in queries]
    
# Example usage
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(calc_equation(equations, values, queries))