from collections import deque

# Longest subarray
def longest_subarray(nums, limit):
    # This is solved using the slidingwindow approach
    
    # Double ended queues to store the min and max values if the current window
    min_queue = deque()
    max_queue = deque()
    
    left, result = 0, 0
    
    for right, num in enumerate(nums):
        # Maintain the max queue in decreasing order
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        # Maintain the min queue in increasing order
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
        # If the difference between the max queue and the min queue exceeds the limit, shrink the window
        while max_queue[0] - min_queue[0] > limit:
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            if min_queue[0] == nums[left]:
                min_queue.popleft()
            
            left += 1
            
        result = max(result, right - left + 1)
    
    return result

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)


# # Length of thelongest substring
# def length_of_longest_substring(s):
#     char_index_map = {}
#     left, max_length = 0, 0
    
#     for right in range(len(s)):
#         # If character is already in the index map and the value at the right pointer is greater than or equals to the left pointer, update the left pointer to the by moving the value at the right pointer one place to the right
#         if s[right] in char_index_map and char_index_map[s[right]] >= left:
#             left = char_index_map[s[right]] + 1
            
#         char_index_map[s[right]] = right
        
#         max_length = max(max_length, right - left + 1)
        
#     return max_length
 
#  # Example usage
# s = "abcabcbb"
# print(length_of_longest_substring(s))



# from collections import deque

# # Letter combinations
# def letter_combinations(digits):
#     if not digits:
#         return []
    
#     phone_map = {
#         '2': 'abc',
#         '3': 'def',
#         '4': 'ghi',
#         '5': 'jkl',
#         '6': 'mno',
#         '7': 'pqrs',
#         '8': 'tuv',
#         '9': 'wxyz'
#     }
    
#     # # Solution using iteration
#     # queue = deque([''])
    
#     # for digit in digits:
#     #     for _ in range(len(queue)):
#     #         combination = queue.popleft()
            
#     #         for letter in phone_map[digit]:
#     #             queue.append(combination + letter)
                
#     # return list(queue)
    
#     # Solution using recursion
#     result = []
    
#     # Backtracking function to generate combinations
#     def backtrack(combination, next_digits):
#         if not next_digits:
#             result.append(combination)
#         else:
#             for letter in phone_map[next_digits[0]]:
#                 backtrack(combination + letter, next_digits[1:])
    
#     backtrack('', digits)
    
#     return result


# # Example usage
# number = '56'
# print(letter_combinations(number))


# # String Subsequence
# def is_subsequence(s, t):
#     # Initialize a pointer to keep track of the cirrent position in string t
#     t_index = 0
    
#     for char in s:
#         # Move the pointer forward in string t until we find a match or reach the end
#         while t_index < len(t) and t[t_index] != char:
#             t_index += 1
            
#         # If we've reached the end of string t without finding a match, return False.
#         if t_index == len(t):
#             return False
        
#         t_index += 1
        
#     return True
        
        
# # Example usage:
# s = "ace"
# t = "abcde"
# print(is_subsequence(s, t))
    


# # Longest Repeating Character Replacement
# def longest_repeating_character_replacement(s, k):
#     # This is solved using the sliding window approach
#     char_count = {}
#     left, max_count, max_length = 0, 0, 0
    
#     for right in range(len(s)):
#         # Increment the count for the current character
#         char_count[s[right]] = char_count.get(s[right], 0) + 1
        
#         # Update the max_count to be the highest count of any character in the window
#         max_count = max(max_count, char_count[s[right]])
        
#         # If the number of characters that need to be replaced is more than k, shrink the window from the left
#         if right - left + 1 - max_count > k:
#             char_count[s[left]] -= 1
#             left += 1
            
#         max_length = max(max_length, right - left + 1)
        
#     return max_length

# # Example usage:
# s = "AABABBA"
# k = 1
# result = longest_repeating_character_replacement(s, k)
# print(result)

# from collections import defaultdict

# def binary_search(values, timestamp):
#     left, right = 0, len(values)
    
#     while left < right:
#         mid = (left + right) // 2
        
#         if values[mid][0] <= timestamp:
#             left = mid + 1
#         else:
#             right = mid
            
#     return left


# class TimeMap:
    
#     def __init__(self):
#         self.data = defaultdict()
        
        
#     def set(self, key, value, timestamp):
#         self.data[key].append((timestamp, value))
        
    
#     def get(self, key, timestamp):
#         if key not in self.data:
#             return ''
        
#         values = self.data[key]
#         idx = binary_search(values, timestamp)
        
#         if idx == 0:
#             return ''
        
#         return values[idx - 1][1]
        