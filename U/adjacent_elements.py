"""You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

Set colors[indexi] to colori.
Count adjacent pairs in colors set to the same color (regardless of colori).
Return an array answer of the same length as queries where answer[i] is the answer to the ith query."""

def colorTheArray(n, queries):
    colors = [0] * n
    same_color_count = 0
    result = []
    
    for idx, new_color in queries:
        left_neighbor, right_neighbor = idx - 1, idx + 1
                
        # If the index is already colored, removed its previous effect
        if colors[idx] != 0:
            if left_neighbor >= 0 and colors[left_neighbor] == colors[idx]:
                same_color_count -= 1
            if right_neighbor < n and colors[right_neighbor] == colors[idx]:
                same_color_count -= 1
                
        colors[idx] = new_color
        
        if left_neighbor >= 0 and colors[left_neighbor] == colors[idx]:
            same_color_count += 1
        if right_neighbor < n and colors[right_neighbor] == colors[idx]:
            same_color_count += 1
        
        result.append(same_color_count)
    
    return result

n = 5
queries = [[1, 2], [2, 2], [1, 3], [3, 3]]
print(colorTheArray(n, queries))