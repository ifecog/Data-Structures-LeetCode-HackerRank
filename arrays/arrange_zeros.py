def arrange_zero_and_nonzero_elements(nums):
    """Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in place without making a copy of the array.

    Args:
        nums (int): the given array

    Returns:
        int: an array of nums with the 0 elements placed at the end of the array
    """
    
    n = len(nums)
    
    zero_index = 0
    
    for i in range(n):
        if nums[i] != 0:
            nums[zero_index], nums[i] = nums[i], nums[zero_index]
            zero_index += 1    
            
array = [0, 2, 5, 0, 4, 0, 2, 2, 6, 0]
arrange_zero_and_nonzero_elements(array)
print(array)

def duplicate_zeros(arr):
    n = len(arr)
    zeros = arr.count(0)
    
    i, j = n - 1, n + zeros - 1
    
    while i >= 0:
        if j < n:
            arr[j] = arr[i]
            
        if arr[i] == 0:
            j -= 1
            
            if j < n:
                arr[j] = 0
                
        i -= 1
        j -= 1
        
        
# Example Usage:
arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr)
print(arr)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]

            
            
