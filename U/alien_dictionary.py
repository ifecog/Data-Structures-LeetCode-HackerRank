from collections import defaultdict, deque

def alienOrder(words):
    n = len(words)
    
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}
    
    # Build the graph by comparing adjacent words
    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))
        
        # Edge cases: 'abc' -> 'ab' is invalid (prefix issue)
        if len(w1) > len(w2) and w1[:min_length] == w2:
            return ''
        
        for j in range(min_length):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
            
                break 
        
    # Perform BFS
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []
    
    while queue:
        char = queue.popleft()
        order.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return ''.join(order) if len(order) == len(in_degree) else ''
    
     
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))           
    