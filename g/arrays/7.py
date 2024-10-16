def check_subarray_sum(nums, k):
    # Dictionary to store the remainder of prefix sum divided by k and its index
    prefix_mod = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        # Update current sum
        current_sum += num
        
        if k != 0:
            current_sum %= k
            
        # Check if this remainder has been seen before
        if current_sum in prefix_mod:
            # Check if the subarray length is at least 2
            if i - prefix_mod[current_sum] >= 2:
                return True
        
        else:
            # Store the current index for this remainder
            prefix_mod[current_sum] = i
    
    return False
    
    
# Example usage
nums = [23,2,4,6,7]
k = 6
print(check_subarray_sum(nums, k))