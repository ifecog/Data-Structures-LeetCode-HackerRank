def next_permuation(nums):
    """The next permutation of an array of integers is the next lexicographically greater permutation of its integer. Given an array of integer nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

    Args:
        nums (int): the given array (current permutation)
        
    Returns:
        int: the next permutation of numbers
    """
    
    # find the decreasing element
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    # find the smallest element to the right that is greater than nums[i]
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # reverse the right subarray (reverse the array to the right of nums[i])
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        

# example test
num_perm = [1, 2, 3, 4]
next_permuation(num_perm)
print('Next Permutation:', num_perm)