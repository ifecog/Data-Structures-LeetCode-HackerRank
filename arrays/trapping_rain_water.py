def trap(height):
    """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Args:
        height (int): bar heights
    """
    
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0
    
    while left < right:
        # If left_max < right_max, move left pointer one place to the right
        if left_max < right_max:
            left += 1
            
            # Update left_max
            left_max = max(left_max, height[left])
            
            # Calculate trapped water at the current left position
            water_trapped += left_max - height[left]
        else:
            # Process from the right
            right -= 1
            
            # Update right_max
            right_max = max(right_max, height[right])
            
            # Calculate trapped water at the current right position
            water_trapped += right_max - height[right]
    
    return water_trapped

# Time Complexity: O(n), Space Complexity: O(1)

# Example usage
length = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(length))
