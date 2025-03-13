from collections import defaultdict, deque

def maximumDetonation(bombs):
    n = len(bombs)
    
    # Build the graph as an adjacency list
    adj_list = defaultdict(list)
    
    for i in range(n):
        x1, y1, r1 = bombs[i]
        
        for j in range(n):
            if i != j:
                x2, y2, _ = bombs[j]
                
                # Check if bomb[j] liies within the radius of bomb[i]
                if ((x2 - x1) ** 2) + ((y2 - y1) ** 2) <= r1 ** 2:
                    adj_list[i].append(j)
                    
    def bfs(start):
        visited = {start}
        queue = deque([start])
        count = 1
        
        while queue:
            node = queue.popleft()
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    count += 1
            
        return count
    
    max_detonations = 0
    for i in range(n):
        max_detonations = max(max_detonations, bfs(i))
    
    return max_detonations
        
                
# Example usage
bombs = [[2, 1, 3], [6, 1, 4]]
print("Maximum Bombs Detonated:", maximumDetonation(bombs))      
                    
    