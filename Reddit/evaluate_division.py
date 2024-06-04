from collections import defaultdict

def calc_equation(equations, values, queries):
    """You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be determined, return -1.0.

    Args:
        equations (array): an array of variable pair equations
        values (int): number values
        queries (array): an array of variable pairs to be queried

    Returns:
        _type_: _description_
    """
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
        
        visited.add(start)
        
        for neighbor in graph[start]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            
            temp = dfs(neighbor, end, visited)
            if temp != -1.0:
                return temp * graph[start][neighbor]
        
        return -1.0
    
    return[dfs(c, d, set()) if c in graph and d in graph else -1.0 for c, d in queries]
    
    
# Example usage
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(calc_equation(equations, values, queries))