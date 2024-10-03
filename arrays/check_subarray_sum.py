def check_subarray_sum(nums, k):
    # Dictionary to store cumulative sum modulo k and its index
    remainder_count = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        # Update cumulative sum modulo k
        current_sum  = (current_sum + num) % k
        
        # Check if cumulative sum modulo exists in dictionary
        if current_sum in remainder_count:
            # Check if subarray length is at least 2
            if i - remainder_count[current_sum] >= 2:
                return True
        
        else:
            remainder_count[current_sum] = i
    
    return False


# Example usage
nums = [23,2,4,6,7]
k = 6
print(check_subarray_sum(nums, k))