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


def indices_sum(nums, target):
    """given an array of integers and an integer target, return indices of the 2 numbers such that they add up to target

    Args:
        num (int): an array of integers
        target (int): a target number for 2 pairs of elements
    """
    
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  


array = [2, 3, 4, 5, 7, 6]
target = 11
print(indices_sum(array, target))

