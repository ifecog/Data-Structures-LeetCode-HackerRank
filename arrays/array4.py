def next_permutation(nums):
    """The next permutation of an array of integers is the next lexicographically greater permutation of its integer. Given an array of integer nums, find the next permutation of nums. The replacement must be in place and use only constant extra memory.

    Args:
        nums (int): the given array (current permutation)
        
    Returns:
        int: the next permutation of numbers
    """
    
    # Find the decreasing element
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    # Find the smallest element to the right that is greater than nums[i]
    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # Reverse the array to the right of nums[i] (the right subarray)
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
# Time Complexity: O(n)
# Space Complexity: O(1)

# Example usage
num_perm = [1, 2, 3, 4]
next_permutation(num_perm)
print('Next Permutation:', num_perm)