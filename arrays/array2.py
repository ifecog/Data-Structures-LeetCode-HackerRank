def arrange_zero_and_nonzero_elements(nums):
    """Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in place without making a copy of the array.

    Args:
        nums (int): the given array

    Returns:
        int: an array of nums with the 0 elements placed at the end of the array
    """
    
    n = len(nums)
    non_zero_index = 0
    
    # create 2 pointers... one to iterate through the array and two to move non-zero elements on the specified locations
    for i in range(n):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1  
        
            
array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
arrange_zero_and_nonzero_elements(array)
print(array)

            
            
