def intersection(nums):
    """
    Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

    Args:
        nums (array): A 2D integer array
    """
    
    # Start with the set of the first array
    common_elements = set(nums[0])
    
    # Find the intersection of the current set with each subsequent array
    for arr in nums[1:]:
        common_elements.intersection_update(arr)
        
    return sorted(common_elements)

nums = [[3, 1, 2], [1, 4, 3, 2], [1, 2]]
print(intersection(nums))