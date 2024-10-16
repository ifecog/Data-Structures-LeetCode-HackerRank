def subarray_sum(nums, k):
    # Dictionary to store the count of prefix sums
    prefix_sums = {0: 1}
    current_sum, count = 0, 0
    
    for num in nums:
        current_sum += num
        
        complement = current_sum - k
        
        # Check if the complement is in prefix sum
        if complement in prefix_sums:
            count += prefix_sums[complement]
            
        if current_sum in prefix_sums:
            