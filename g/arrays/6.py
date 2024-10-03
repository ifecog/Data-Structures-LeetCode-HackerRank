def subarray_sum(nums, k):
    prefix_sums = {0: 1}
    current_sum, count = 0, 0
    
    for num in nums:
        current_sum += num
        
        complement = current_sum - k
        
        if complement in prefix_sums:
            count += prefix_sums[complement]
            
        if current_sum in prefix_sums:
            prefix_sums[current_sum] += 1
        else:
            prefix_sums[current_sum] = 1
    
    return count

nums = [1,1,1]
k = 2
print(subarray_sum(nums, k))



# Brute Force
# def subarray_sum(nums, k):
#     count = 0
#     for i in range(len(nums)):
#         sum = 0
#         for j in range(i, len(nums)):
#             sum += nums[j]
#             if sum == k:
#                 count += 1
                
    
#     return count

# nums = [1,1,1]
# k = 2
# print(subarray_sum(nums, k))