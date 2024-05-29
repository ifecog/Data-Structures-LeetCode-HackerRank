def array_median(nums1, nums2):
    """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall runtime complexity should be 0(log(m+n))

    Args:
        nums1 (array): an array of integers
        nums2 (array): an array of integers
    """
    
    # Define a nested function to merge the arrays
    def merge_arrays(arr1, arr2):
        # Ensure that arr1 has the capacity hold all the elements in the combination of both arrays
        # This is done by extending arr1 with 0s to match the length of the combined array
        arr1 += [0] * len(arr2)
        
        # Initialize pointers
        p1, p2, p_merged = len(arr1) - len(arr2) - 1, len(arr2) - 1, len(arr1) - 1
        
        while p1 >= 0 and p2 >= 0:
            if arr1[p1] >= arr2[p2]:
                arr1[p_merged] = arr1[p1]
                p1 -= 1
            else:
                arr1[p_merged] = arr2[p2]
                p2 -= 1
            p_merged -= 1
            
        if p2 >= 0:
            arr1[:p2 + 1] = arr2[:p2 + 1]
        
        return arr1
    
    # Implement the merge_arrays function to merge nums1 and nums2
    nums = merge_arrays(nums1, nums2)
    print('Merged Array:', nums)
    n = len(nums)
    
    if n % 2 == 0:
        return (nums[(n // 2) - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]
    
    
# Example usage:
nums1 = [1, 2, 6, 9]
nums2 = [3, 4, 7, 8, 9, 10]
result = array_median(nums1, nums2)
print('Median:', result) 