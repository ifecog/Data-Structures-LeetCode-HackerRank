def arrange_zero_and_nonzero_elements(nums):
    """Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in place without making a copy of the array.

    Args:
        nums (int): the given array

    Returns:
        int: an array of nums with the 0 elements placed at the end of the array
    """
    
    zero_index = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1    
            
array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
arrange_zero_and_nonzero_elements(array)
print(array)

            
            
