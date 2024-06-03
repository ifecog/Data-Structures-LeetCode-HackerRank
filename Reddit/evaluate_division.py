from collections import defaultdict

def calc_equation(equation, values, queries):
    # CReate a graph as a dictionary where each key is a variable and each value is a list of tuples
    graph = defaultdict(list)
    
    for (a, b), v in zip(equation, values):
        graph[a].append((b, v))
        graph[b].append((a, 1/v))       
        
    # Define a nested function to perform DFS
    def dfs(a, b, visited):
        if a not in graph or b not in graph:
            return -1.0
        
        