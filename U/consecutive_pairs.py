"""
You are given a number line of length N. You're given a 2d array query, where query[i][0] is the coordinate which this query colors with query[i][1] color. For each query, you need to tell the number consecutive pairs of same color in the number line. Initially all numbers are not colored and can be assumed to be 0. 

Example:
Input: query=[[2,1],[3,1],[4,3],[5,1],[4,1]] 
Output: [0,1,1,1,3]    
"""

def count_consecutive_pairs(query):
    max_n = max(x[0] for x in query)
    line = [0] * (max_n + 1) # Number line initialized to 0
    same_color_pairs = 0 # Counter for consecutive pairs
    result = []
    
    for idx, color in query:
        # Check the left and right neighbors
        left_same = (idx > 0 and line[idx - 1] == line[idx] and line[idx] != 0)
        right_same = (idx < max_n and line[idx + 1] == line[idx] and line[idx] != 0)
        
        # Remove previous contributions
        if left_same:
            same_color_pairs -= 1
        if right_same:
            same_color_pairs -= 1
            
        # Update the color
        line[idx] = color
        
        # Update left_same and right_same
        left_same = (idx > 0 and line[idx - 1] == line[idx])
        right_same = (idx < max_n and line[idx + 1] == line[idx])
        
        # Add current contributions
        if left_same:
            same_color_pairs += 1
        if right_same:
            same_color_pairs += 1
            
        result.append(same_color_pairs)
    
    return result
    
  
# Example usage
query = [[2,1],[3,1],[4,3],[5,1],[4,1]]
print(count_consecutive_pairs(query))