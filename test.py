    # """Given an array of strings strs, groupd the anagrams together. 
    # """
def group_anagrams(strs):
    anagrams = {}
        
    for word in strs:
        sorted_words = ''.join(sorted(word))
            
        if sorted_words in anagrams:
            anagrams[sorted_words].append(word)
        else:
            anagrams[sorted_words] = [word]
                
    return list(anagrams.values())


# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)



# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
        
        
# class LinkedList:
#     def __init__(self):
#         self.head = None
        
    
#     def reverse_linked_list(head):
#         """
#             Given the head of a singly linked list, reverse the list, and return the reversed list
#         """
        
#         prev = None
#         current = head





    # """You are given a string s asnd an integer k. You can choose any character of the string and change it to any uppercase English character. You can perform this operation at most k times.
    # """
    
# def character_replacement(s, k):
#     # initialize variables
#     max_length = 0
#     max_count = 0
#     char_count = {}
#     left = 0
    
#     for right in range(len(s)):
#         # increment the count of the character at the right pointer
#         char_count[s[right]]  = char_count.get(s[right], 0) + 1
        
#         # update the maximum count
#         max_count = max(max_count, char_count[s[right]])
        
#         # check if the current window needs shrinking
#         if right - left + 1 - max_count > k:
#             char_count[s[left]] -= 1
#             left += 1
        
#         # update maximum length
#         max_length = max(max_length, right - left + 1)
        
        
    
#     return max_length
    

# # Example usage:
# s = "AABABBA"
# k = 1
# result = character_replacement(s, k)
# print(result)


# from collections import Counter

# def min_window(s, t):
#     left, right = 0, 0
#     min_len = len(s) + 1
#     min_win_substr = ''
#     required_chars = Counter(t)
#     missing_chars = len(t)
    
#     while right < len(s):
#         if s[right] in required_chars:
#             required_chars[s[right]] -= 1
            
#             if required_chars[s[right]] >= 0:
#                 missing_chars -= 1
                
#         while missing_chars == 0:
#             if right - left + 1 < min_len:
#                 min_len = right - left + 1
#                 min_win_substr = s[left:right + 1]
                
#             if s[left] in required_chars:
#                 required_chars[s[left]] += 1
                
#                 if required_chars[s[left]] > 0:
#                     missing_chars += 1
            
#             left += 1
                
#         right += 1
    
#     return min_win_substr
    

# # Example usage:
# s = "ADOBECODEBANC"
# t = "ABC"
# result = min_window(s, t)
# print(result)



# def merge_arrays(nums1, m, nums2, n):
#     # initialize pointers for nums1, nums2, and the merged result
#     p1, p2, p_merged = m - 1, n - 1, m + n - 1
    
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] > nums2[p2]:
#             nums1[p_merged] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p_merged] = nums2[p2]
#             p2 -= 1
#         p_merged -= 1
        
#     # insert elements in nums2 that are not already in nums1
#     nums1[:p2 + 1] = nums2[:p2 + 1]
    
#     return nums1


# # Example usage:
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# merge_arrays(nums1, m, nums2, n)
# print(nums1)


# def min_subarray_length(nums, target):
#     # initiate variables
#     min_length = len(nums) + 1
#     left, current_sum = 0, 0
    
#     # iterate through the array using the sliding windows approach
#     for right, num in enumerate(nums):
#         # update the current sum with the surrent num
#         current_sum += num
        
#         while current_sum >= target:
#             min_length = min(min_length, right - left + 1)
            
#             # remove the leftmost element in the current window
#             current_sum -= nums[left]
#             left -= 1
            
#     return min_length if min_length <= len(nums) else 0
    

# def merged_interval(intervals):
#     intervals.sort(key=lambda i: i[0[)

#     merged = []
#     for interval in intervals:
#         if not merged or interval[0] > merged[-1][1]:
#             merged.append(interval)
# 	else:
# 	    merged[-1][1] = max(merged[-1][1], interval[1])
    
#     return merged



# def kth_smallest(matrix, k):
#     n = len(matrix)
#     low, high = matrix[0][0], matrix[-1][-1]
    
#     def count_less_equal(array, target):
#         n, count = len(array), 0
#         row, col = n - 1, 0
        
#         while row >= 0 and col < n:
#             if array[row][col] <= target:
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
#             low = mid + 1
#         else:
#             high = mid
            
#     return low
    
    
# # example
# matrix = [
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# k = 8
# result = kth_smallest(matrix, k)
# print(result)


# def product_of_elements(nums):
#     n = len(nums)
#     left_products, right_products = [1] * n, [1] * n
    
#     left_product = 1
#     for i in range(1, n):
#         left_product *= nums[i - 1]
#         left_products[i] = left_product
    
#     right_product = 1
#     for i in range(n - 2, -1, -1):
#         right_product *= nums[i + 1]
#         right_products[i] = right_product
        
#     result = [left_products[i] * right_products[i] for i in range(n)]
    
#     return result

# # test code
# array = [2, 4, 6, 8, 10]
# result = product_of_elements(array)
# print(result)



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