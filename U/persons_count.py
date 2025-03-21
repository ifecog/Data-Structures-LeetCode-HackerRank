def canSeePersonsCount(heights):
    n = len(heights)
    result = [0] * n
    
    # Monotonic decreasing stack
    stack = []
    
    # Traverse from right to left
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

heights = [10, 6, 8, 5, 11, 9]
print(canSeePersonsCount(heights))