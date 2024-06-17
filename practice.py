def minimum_time(time, totalTrips):
    left = 1
    right = min(time) * totalTrips
    
    return left


# def length_of_longest_substring(s):
#     char_set = set()
#     left = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         # If the current character is already in the cell, remove characters from the left
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
        
#         # Add the current character to the set
#         char_set.add(s[right])
        
#         # Update the maximum length
#         max_length = max(max_length, right - left + 1)
    
#     return max_length


# # Example usage
# s = "abcabcbb"
# print(length_of_longest_substring(s))


# from collections import deque

# def longest_subarray(nums, limit):
#     max_queue = deque()
#     min_queue = deque()
    
#     left = 0
#     result = 0
    
#     for right, num in enumerate(nums):
#         while max_queue and num > max_queue[-1]:
#             max_queue.pop()
#         max_queue.append(num)
        
#         while min_queue and num < min_queue[-1]:
#             min_queue.pop()
#         min_queue.append(num)
        
#         # If the difference between the max queue and the min queue exceeds the limit, shrink the window
#         while max_queue[0] - min_queue[0] > limit:
#             if max_queue[0] == nums[left]:
#                 max_queue.popleft()
#             if min_queue[0] == nums[left]:
#                 min_queue.popleft()
#             left += 1
            
#         result = max(result, right - left + 1)
    
#     return result

# # Example usage:
# nums = [8, 2, 4, 7]
# limit = 4
# output = longest_subarray(nums, limit)
# print(output)

# def leftmost_column_with_one(binaryMatrix):
#     row, col = 0, len(binaryMatrix) - 1
#     leftmost_col = -1
    
#     while row < len(binaryMatrix) and col >= 0:
#         if binaryMatrix[row][col] == 1:
#             leftmost_col = col
#             col -= 1
#         row += 1
    
#     return leftmost_col

# # Example usage:
# binaryMatrix = [
#     [0, 0, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 1, 1],
#     [0, 0, 0, 0]
# ]

# print(leftmost_column_with_one(binaryMatrix)) 


# def height_checker(heights):
#     expected = sorted(heights)
    
#     # count = 0
#     # for i in range(len(heights)):
#     #     if heights[i] != expected[i]:
#     #         count += 1
    
#     count = sum(h1 != h2 for h1, h2 in zip(heights, expected))
        
#     return count

# # Example usage:
# heights = [1,1,4,2,1,3]
# result = height_checker(heights)
# print(result) 


# def character_replacement(s, k):
#     char_count = {}
#     left = 0
#     max_count = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         char_count[s[right]] = char_count.get(s[right], 0) + 1
        
#         # Update the maximum count
#         max_count = max(max_count, char_count[s[right]])
        
#         if right - left + 1 - max_count > k:
#             char_count[s[left]] -= 1
#             left += 1
        
#         # Update the maximum length
#         max_length = max(max_length, right - left + 1)
    
#     return max_length

# # Example usage:
# s = "AABABBA"
# k = 1
# result = character_replacement(s, k)
# print(result)

