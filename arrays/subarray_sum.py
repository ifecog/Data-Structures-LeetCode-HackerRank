def subarray_sum(nums, k):
    """Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array

    Args:
        nums (int): An array of integers
    """

    # Dictionary to store the count of prefix sums
    prefix_sums = {0: 1}
    current_sum, count = 0, 0
    
    for num in nums:
        current_sum += num
        
        complement = current_sum - k
        
        # Check if complement is in prefix_sums
        if complement in prefix_sums:
            count += prefix_sums[complement]
            
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1
    
    return count

    
    # # Brute Force
    # count = 0
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(i, len(nums)):
    #         sum += nums[j]
    #         if sum == k:
    #             count += 1
    
    # return count
    

nums = [1,1,1]
k = 2
print(subarray_sum(nums, k))