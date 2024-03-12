def array_median(nums1, nums2):
    """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall runtime complexity should be 0(log(m+n))

    Args:
        nums1 (array): an array of integers
        nums2 (array): an array of integers
    """
    
    def merge_arrays(arr1, arr2):
        arr1 += [0] * len(arr2)
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
    
    merged_array = merge_arrays(nums1, nums2)
    array_len = len(merged_array)
    
    if array_len % 2 == 0:
        return (merged_array[array_len // 2 - 1] + merged_array[array_len // 2]) / 2
    else:
        return merged_array[array_len // 2]
    
    
# Example usage:
nums1 = [1, 2]
nums2 = [3, 4]
result = array_median(nums1, nums2)
print(result) 