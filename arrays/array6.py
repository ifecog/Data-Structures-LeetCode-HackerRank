def rotate_array(nums, k):
    """Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

    Args:
        nums (int): the given array
        k (_type_): no of steps
    """
    
    # ensure that k is less than the length of nums
    k = k % len(nums)
    
    # # 1. use array slicing
    nums[:] = nums[-k:] + nums[:-k]
    
    # 2. use the reverse function
    # nums.reverse()
    
    # nums[:k] = reversed(nums[:k])
    # nums[k:] = reversed(nums[k:])
    
    return nums
    


# text examole
nums = [-1,-100,3,99]
k = 2
print(rotate_array(nums, k))