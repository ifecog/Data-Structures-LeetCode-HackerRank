from collections import defaultdict

def calc_equation(equations, values, queries):
    # This is solved using the Depth-First-Search approach
    
    # Build the graph
    graph = defaultdict(dict)
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1/value
        
    def dfs(start, end, visited):
        # if neither start or end variable is not in the graoh, return -1.0
        if start not in graph or end not in graou