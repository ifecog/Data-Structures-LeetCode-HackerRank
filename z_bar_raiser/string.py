# 4. Merge Arrays
def merge_arrays(nums1, m, nums2, n):
    # This is solved using pointers for each arrays
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
    
    # If there are remaining elements in nums2, add them to the merged array, nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]
    
    return nums1 

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge_arrays(nums1, m, nums2, n)
print(nums1)


# # 3. Rotate array by k steps
# def rotate_array(nums, k):
#     # Ensure that k is less than the lenth of the array nums
#     k = k % len(nums)
    
#     # Use array Slicing
#     # nums[:] = nums[-k:] + nums[:-k]
    
#     # Use the reverse function
#     nums.reverse()
    
#     nums[:k] = reversed(nums[:k])
#     nums[k:] = reversed(nums[k:])
    
#     return nums
    
# # Test example
# nums = [-1,-100,3,99, 78]
# k = 2
# print(rotate_array(nums, k))


# # 2. Find first non-repeating charactrer
# def first_unique_char(s):
#     # This is solved by storing the frequency of character occurence in a dict
#     count = {}
    
#     for char in s:
#         count[char] = count.get(char, 0) + 1
        
#     for index, char in enumerate(s):
#         if count[char] == 1:
#             return index
        
#     return -1

# print(first_unique_char("leetcode"))       # Output: 0
# print(first_unique_char("loveleetcode"))   # Output: 2
# print(first_unique_char("aabb"))          
        


# # 1. Reverse String
# def reverse_string(s):
#     # This is solved using pointers
    
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
        
# # example test
# test_string = ['a', 'y', 'o', 'm', 'i', 'd', 'e']
# reverse_string(test_string)
# print(test_string)