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
                result.append((i, j))
    
    return result if result else None    


array = [2, 3, 4, 5, 7, 6]
target = 11
print(indices_sum(array, target))

