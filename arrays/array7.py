def two_sum(nums, target):
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Args:
        nums (int): an array of integers
        target (int): the target integer
    """
   
    # Initialize an empty dictionary to store the index of numbers
    nums_indices = {}
    
    # use enumerate to loop through nums to get index and num
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in nums_indices:
            return [nums_indices[complement], i]
        
        nums_indices[num] = i
    
    return []

# Example usage:
nums = [2, 7, 6, 5]
target = 9
result = two_sum(nums, target)
print(result)