def two_sum(nums, target):
    nums_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_index:
            return [nums_index[complement], i]

        nums_index[num] = i
    
    return []


# Example usage:
nums = [2, 7, 6, 5]
target = 9
result = two_sum(nums, target)
print(result)