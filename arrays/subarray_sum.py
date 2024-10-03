def subarray_sum(nums, k):
    """Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array

    Args:
        nums (int): An array of integers
    """
    
    # Dictionary to store the count pf prefix sums
    prefix_sums = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        
        # Check if current sum exists in the prefix_sums dictionary
        # If it does, then we found a subarray summing to k
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
            
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1
    
    return count

nums = [1,1,1]
k = 2
print(subarray_sum(nums, k))