def intersection(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

    Args:
        nums1 (array): an array of integers
        nums2 (array): an array of integers
    """
    
    # Convert the arrays to set to avoid duplicates
    # set1 = set(nums1)
    # set2 = set(nums2)
    
    # result = set1.intersection(set2)
    
    # return list(result)

    return list(set(nums1) & set(nums2))

# Example usage
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))