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
                
#                 # Skip duplicates for the second number
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
                
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
                    
#                 left += 1
#                 right -= 1
                    
#             elif current_sum < 0:
#                 left += 1
#             elif current_sum > 0:
#                 right -= 1
    
#     return result

# # Example usage
# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

def find_three_numbers(nums, target):
    nums.sort()
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == target:
                return [nums[i], nums[left], nums[right]]
            
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
                
    return []
        

# Example usage
nums = [12, 3, 4, 1, 6, 9]
target = 24
print(find_three_numbers(nums, target)) 