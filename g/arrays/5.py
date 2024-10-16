def trap(height):
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
            right -= 1
            
            # Update right_max
            right_max = max(right_max, height[right])
            
            # Calculate trapped water at the current right position
            water_trapped += right_max - height[right]
    
    return water_trapped