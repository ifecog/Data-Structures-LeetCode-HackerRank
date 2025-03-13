def canTransform(start, result):
    n = len(start)
    
    # Check if the strings contain the same characters
    if start.replace('X', '') != result.replace('X', ''):
        return False
    
    # Compare L and R positions
    j = 0
    for i, char in enumerate(start):
        if char == 'X':
            continue
        
        # Move the result's pointer to match a non-X character
        while j < n and result[j] == 'X':
            j += 1
        
        if j >= n or char != result[j]:
            return False
        
        if char == 'L' and i < j:
            return False
        if char == 'R' and i > j:
            return False
        j += 1
        
    return True

# Example usage
north = "RXXLRXRXL"
south = "XRLXXRRLX"
print(canTransform(north, south))
