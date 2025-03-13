from collections import defaultdict

def maxScore(scores, edges):
    adj = defaultdict(list)
    
    # Build the adjacency list
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # Reduce adjacency list to keep only top 3 highest-scoring neighbors
    for node in adj:
        adj[node] = sorted(adj[node], key=lambda x: -scores[x])[:3]
        
    max_score = -1
    
    # Try forming a sequence (A -> B -> C -> D) for each edge (B, C)
    for b, c in edges:
        for a in adj[b]:
            if a == c:
                continue
            
            for d in adj[c]:
                if d == b or d == a:
                    continue
                
                score = scores[a] + scores[b] + scores[c] + scores[d]
                
                max_score = max(max_score, score)
                
    return max_score


# Example Usage:
scores = [5, 2, 9, 8, 4]  
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 4], [2, 4]]
print("Maximum score of valid node sequence:", maxScore(scores, edges))