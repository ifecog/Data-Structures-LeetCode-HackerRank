# Letter Combination
def letter_combinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    queue = ['']
    
    for digit in digits:
        for _ in range(len(queue)):
            combination = queue.pop(0)
            
            for letter in phone_map[digit]:
                queue.append(combination + letter)
    
    return queue

# Example usage
number = '56'
print(letter_combinations(number))

# # Longest Repeating Character Replacement
# def longest_repeating_character_replacement(s, k):
#     char_freq = {}
#     left, max_count, max_length = 0, 0, 0
    
#     for right in range(len(s)):
#         char_freq[s[right]] = char_freq.get(s[right], 0) + 1
        
#         max_count = max(max_count, char_freq[s[right]])
        
#         # If the number of characters that needs to be replaced is greater than k, shrink the window from the left
#         if right - left + 1 - max_count > k:
#             char_freq[s[left]] -= 1
#             left += 1
        
#         max_length = max(max_length, right - left + 1)
    
#     return max_length

# # Example usage:
# s = "AABABBA"
# k = 1
# result = longest_repeating_character_replacement(s, k)
# print(result)


# # Subsequence
# def is_subsequence(s, t):
#     # Initialize a pointer to keep track of the current position in string t
#     t_index = 0
    
#     for char in s:
#         # Move the pointer forward in string t until we find a match or reach the end
#         while t_index < len(t) and t[t_index] != char:
#             t_index += 1
            
#         # If we reach the end of string t without finding a match, return False
#         if t_index == len(t):
#             return False
        
#         # Move the pointer forward to the next character in t
#         t_index += 1
    
#     return True

# # Example usage:
# s = "ace"
# t = "abcde"
# print(is_subsequence(s, t))


# # Fequency Sort
# def frequency_sort(s):
#     char_freq = {}
#     sorted_str = ''
    
#     for char in s:
#         # Count the frequency of each character in s
#         char_freq[char] = char_freq.get(char, 0) + 1
        
#     sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    
#     for char in sorted_chars:
#         sorted_str += char * char_freq[char]
    
#     return sorted_str

# # Example usage:
# s = "tree"
# result = frequency_sort(s)
# print(result)  


# # Roman to Integer
# def roman_to_int(s):
#     n = len(s)
#     romman_map = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
    
#     total = 0
#     for i in range(n):
#         if i < n - 1 and romman_map[s[i]] < romman_map[s[i + 1]]:
#             total -= romman_map[s[i]]
#         else:
#             total += romman_map[s[i]]
    
#     return total


# # Remove Anagrams
# def remove_anagrams(words):
#     non_anagrams = []
#     for i, word in enumerate(words):
#         if i == 0 or sorted(word) != sorted(words[i - 1]):
#             non_anagrams.append(word)
    
#     return non_anagrams

# # Example usage:
# words = ["dacb", "abdc", "abc", "cba"]
# result = remove_anagrams(words)
# print(result)


# # Minimum Window Substring
# from collections import Counter

# def min_window(s, t):
#     left, right = 0, 0
#     min_length = len(s) + 1
#     min_window_substr = ''
#     required_chars = Counter(t)
#     missing_chars = len(t)
    
#     while right < len(s):
#         # If the char at the right pointer is in t, decrease its count in the required_chars
#         if s[right] in required_chars:
#             required_chars[s[right]] -= 1
            
#             # If the count is non-negative, it means that this character is still needed.
#             if required_chars[s[right]] >= 0:
#                 missing_chars -= 1
                
#         # When all the characters are matched (missing_chars = 0), shrink the window from the left
#         while missing_chars == 0:
#             # Update the min window
#             if right - left + 1 < min_length:
#                 min_length = right - left + 1
#                 min_window_substr = s[left:right + 1]
                
#             # If the char at the right pointer is in t, increase its count in the required_chars
#             if s[left] in required_chars:
#                 required_chars[s[left]] += 1
                
#                 # If the count > 0, we are missing this character again
#                 if required_chars[s[left]] > 0:
#                     missing_chars += 1
            
#             left += 1
        
#         right += 1
    
#     return min_window_substr

# # Example usage:
# s = "ADOBECODEBANC"
# t = "ABC"
# result = min_window(s, t)
# print(result)  # Expected output: "BANC"



# # Find anagrams
# from collections import Counter

# def find_anagrams(s, p):
#     result = []
    
#     len_s, len_p = len(s), len(p)
#     if len_s < len_p:
#         return result
    
#     # Count the occurence of characters in p and the starting window
#     p_counter = Counter(p)
#     window_counter = Counter(s[:len_p])
    
#     # Check if the first window is an anagram
#     if window_counter == p_counter:
#         result.append(0)
        
#     # Slide the window through the rest of s
#     for i in range(len_p, len_s):
#         window_counter[s[i]] += 1
        
#         # Remove the leftmost element after sliding
#         if window_counter[s[i - len_p]] == 1:
#             del window_counter[s[i - len_p]]
#         else:
#             window_counter[s[i - len_p]] -= 1
            
#         # Check if the current window is an anagram
#         if window_counter == p_counter:
#             result.append(i - len_p + 1)
    
#     return result

# # Example usage
# s = "cbaebabacdcab"
# p = "abc"
# result = find_anagrams(s, p)
# print(result) 


# # Reverse String
# def reverse_string(s):
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
        
# # Example usage
# test_string = ['a', 'y', 'o', 'm', 'i', 'd', 'e']
# reverse_string(test_string)
# print(test_string)