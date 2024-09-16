from collections import defaultdict

def calculate_equation(equations, values, queries):
    # Build the graph
    graph = defaultdict(dict)
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1/value
        
    def dfs(start, end, visited):
        # If either start or end variable is not in the graph, return -1.0
        if start not in graph or end not in graph:
            return -1.0
        
        # If start and end are the same, return 1.0
        if start == end:
            return 1.0
        
        # Mark the start node as visited
        visited.add(start)
        
        # Explore all neighbors of the start node
        for neighbor in graph[start]:
            if neighbor in visited:
                continue
            
            # Perform DFS on the neighbor node
            temp = dfs(neighbor, end, visited)
            if temp != -1.0:
                return temp * graph[start][neighbor]
            
        return -1.0
    
    return [dfs(c, d, set()) if c in graph and d in graph else -1.0 for c, d in queries]
        