def twoSum(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left + 1, right + 1]
        
        elif current_sum < target:
            left += 1
            
        else:
            right -= 1
            
    return [-1, -1]

# numbers = [2, 7, 11, 15]
# target = 9
# print(twoSum(numbers, target))  # Output: [1, 2]



# def threeSum(nums):
#     nums.sort()
#     n = len(nums)
    
#     result = []
    
#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
        
#         left, right = i + 1, n - 1
        
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
            
#             if current_sum == 0:
#                 result.append([nums[i], nums[left], nums[right]])
                
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
                
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
                    
#                 left += 1
#                 right -= 1
                
#             elif current_sum < 0:
#                 left += 1
                
#             else:
#                 right -= 1
    
#     return result


# def three_sum(nums, target):
#     nums.sort()
#     n = len(nums)

#     for i in range(n - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
    
#         left, right = i + 1, n - 1
        
#         while left < right:
#             current_sum = nums[i] + nums[left] + nums[right]
            
#             if current_sum == target:
#                 return [nums[i], nums[left], nums[right]]
            
#             elif current_sum < target:
#                 left += 1
            
#             elif current_sum > target:
#                 right -= 1
                
#     return []

# # Example usage
# nums = [12, 3, 4, 1, 6, 9]
# target = 24
# print(three_sum(nums, target))



def two_sum(nums, target):
    nums_indices = {}
   
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_indices:
            return [nums_indices[complement], i]
        
        nums_indices[num] = i
        
    return [] 

# # Example usage:
# nums = [2, 7, 6, 5]
# target = 9
# result = two_sum(nums, target)
# print(result)

