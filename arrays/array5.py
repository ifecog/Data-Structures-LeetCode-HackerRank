def indices_sum(nums, target):
    """given an array of integers and an integer target, return indices of the 2 numbers such that they add up to target

    Args:
        num (int): an array of integers
        target (int): a target number for 2 pairs of elements
    """
    
    n = len(nums)
    
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                result.append((i, j))
                
    return result if result else None


array = [2, 3, 5, 7, 6, 4]
target = 11
print(indices_sum(array, target))
