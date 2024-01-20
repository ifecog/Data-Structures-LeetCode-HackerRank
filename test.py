# def kth_smallest(matrix, k):
#     low, high, n = matrix[0][0], matrix[-1][-1], len(matrix)
    
#     def count_less_equal(matrix, target):
#         n, count = len(matrix), 0
#         row = n - 1, 0
        
#         while row >= 0 and col < n:
#             if matrix[row][col] <= target:
#                 count += row + 1
#                 col += 1
#             else:
#                 row -= 1
                
#         return count
    
#     # implement binary search
#     while low < high:
#         mid = (low + high) // 2
        
#         count = count_less_equal(matrix, mid)
#         if count < k:
#             low = mid - 1:
#         else:
#             high = mid
#     return low

# def reverse_string(s):
#     """Write a function that reverses a string. the input string is given as an array of characters s. You must do this by modifying the input array-in-place with 0(1) extra memory.

#     Args:
#         s (string): an array of characters
#     """
    
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         # swap characters at left and right pointers
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
        

# # example test
# test_string = ['a', 'y', 'o', 'm', 'i', 'd', 'e']
# reverse_string(test_string)
# print(test_string)