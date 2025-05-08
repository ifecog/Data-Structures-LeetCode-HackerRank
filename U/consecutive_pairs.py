"""
You are given a number line of length N. You're given a 2d array query, where query[i][0] is the coordinate which this query colors with query[i][1] color. For each query, you need to tell the number consecutive pairs of same color in the number line. Initially all numbers are not colored and can be assumed to be 0. 

Example:
Input: query=[[2,1],[3,1],[4,3],[5,1],[4,1]] 
Output: [0,1,1,1,3]    
"""

def countConsecutivePairs(query):
    n = max(x[0] for x in query)
    colors = [0] * (n + 1)
    same_color_pairs = 0
    result = []
    
    for idx, new_color in query:
        left_neighbor, right_neighbor = idx - 1, idx + 1
        
        if colors[idx] != 0:
            if left_neighbor >= 0 and colors[left_neighbor] == colors[idx]:
                same_color_pairs -= 1
            if right_neighbor <= n and colors[right_neighbor] == colors[idx]:
                same_color_pairs -= 1
                
        colors[idx] = new_color
        
        if left_neighbor >= 0 and colors[left_neighbor] == colors[idx]:
            same_color_pairs += 1
        if right_neighbor <= n and colors[right_neighbor] == colors[idx]:
            same_color_pairs += 1
        
        result.append(same_color_pairs) 
    
    return result


  
# Example usage
query = [[2,1],[3,1],[4,3],[5,1],[4,1]]
print(countConsecutivePairs(query))