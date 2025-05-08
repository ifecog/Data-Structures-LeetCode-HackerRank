def merge_arrays(nums1, m, nums2, n):
    """You are given 2 integer arrays nums1 and nums2, sorted in non-decreasing order, and 2 intergers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    """
    
    # Initialize pointers for nums1, nums2, and the merged result
    p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
    # Merge from the end of the arrays to avoid overriting elements in nums1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p_merged] = nums1[p1]
            p1 -= 1
        else:
            nums1[p_merged] = nums2[p2]
            p2 -= 1
        p_merged -= 1
        
    # If there are remaining elements in nums2, copy to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    return nums1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_arrays(nums1, m, nums2, n)
print(nums1)

# Time Complexity: O(m + n), Space complexity: O(1)


# def merge_arrays(nums1, m, nums2, n):
#     """You are given 2 integer arrays nums1 and nums2, sorted in non-decreasing order, and 2 intergers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#     """
    
#     # initialize pointers for nums1, nums2, and the merged result
#     nums1 += [0] * n
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     # merge from the end of the arrays to avoid overriting elements in nums1
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] >= nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
#         p_merged -= 1
        
#     # if there are remaining elements in nums2, copy to nums1
#     if p2 >= 0:
#         nums1[:p2 + 1] = nums2[:p2 + 1]
    
#     return nums1

# # Example usage:
# nums1 = [1, 2, 3, 4, 4, 5]
# m = 6
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)