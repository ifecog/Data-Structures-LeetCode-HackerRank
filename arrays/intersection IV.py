def find_difference(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    
    result = [list(set1 - set2), list(set2 - set1)]
    
    return result

# Example usage:
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(find_difference(nums1, nums2))