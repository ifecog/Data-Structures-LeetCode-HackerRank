def check_subarray_sum(nums, k):
    """Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

    A good subarray is a subarray where:

    its length is at least two, and the sum of the elements of the subarray is a multiple of k.
    
    Note that:

    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

    Args:
        nums (int): An array of integers
        k (k): an integer to be summed to

    Returns:
        boolean: True if good subarray else False
    """
    
    # Dictionary to store the remainder of prefix sum divided by k and its index
    
    # This handles the case when a subarray from index 0 sums to a multiple of k
    prefix_mod = {0: -1}
    current_sum = 0
    
    for i, num in enumerate(nums):
        # Update the current sum
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
