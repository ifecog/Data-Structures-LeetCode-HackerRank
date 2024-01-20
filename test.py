def kth_smallest(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]
    
    def count_less_equal(array, target):
        n, count = len(array), 0
        row, col = n - 1, 0
        
        while row >= 0 and col < n:
            if array[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1
                
        return count
    
    # implement binary search
    while low < high:
        mid = (low + high) // 2
        count = count_less_equal(matrix, mid)
        
        if count < k:
            low = mid + 1
        else:
            high = mid
            
    return low
    
    
# example
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
result = kth_smallest(matrix, k)
print(result)






# def two_sum(nums, target):
#     num_indices = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in num_indices:
#             return [num_indices[complement], i]
        
#         num_indices[num] = i
    
#     return []


# array = [2, 3, 5, 7, 6]
# target = 11
# print(two_sum(array, target))




# def binary_search(nums, target):
#     lb, ub, mid = 0, len(nums) - 1, 0
#     steps = 0
    
#     while lb <= ub:
#         print('step', steps, ':', str(nums[lb:ub + 1]))
#         steps += 1
        
#         # def midpoint
#         mid = (lb + ub) // 2
        
#         if target == nums[mid]:
#             return mid
#         else:
#             if target < nums[mid]:
#                 ub = mid - 1
#             else:
#                 lb = mid + 1
                
#     return -1

# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(test_list)
# target = int(input('Target element? '))

# print('Target Location:', binary_search(test_list, target))




# from collections import Counter


# def find_anagrams(s, p):
#     len_s, len_p = len(s), len(p)
#     result = []
    
#     if len_s < len_p:
#         return result
    
#     # def a variable to count all the occurences of characters in p
#     p_counter = Counter(p)
    
#     # def a sliding window counter for the first window of s
#     window_counter = Counter(s[:len_p])
    
#     # check if the first window is an anagram of p
#     if p_counter == window_counter:
#         result.append(0)
        
#     # slide the rest of the window through s
#     for i in range(len_p, len_s):
#         window_counter[s[i]] += 1
        
#         # remove leftmost element from each window counter
#         if window_counter[s[i - len_p]] == 1:
#             del window_counter[s[i - len_p]] 
#         else:
#             window_counter[s[i - len_p]] -= 1
            
#         # check if the current window is an anagram of p
#         if window_counter == p_counter:
#             result.append(i - len_p + 1)
        
#     return result

# # example test
# s = "cbaebabacd"
# p = "abc"
# result = find_anagrams(s, p)
# print(result) 


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