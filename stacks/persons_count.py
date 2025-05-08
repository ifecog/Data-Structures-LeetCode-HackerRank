"""There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue."""

def canSeePersonsCount(heights):
    if not heights:
        return []
    
    n = len(heights)
    
    stack = []
    
    result = [0] * (n)
    
    for i in range(n - 1, -1, -1):
        count = 0
        
        while stack and stack[-1] < heights[i]:
            stack.pop()
            count += 1
            
        if stack:
            count += 1
            
        result[i] = count
        
        stack.append(heights[i])
        
    return result

# Example usage
heights = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights))