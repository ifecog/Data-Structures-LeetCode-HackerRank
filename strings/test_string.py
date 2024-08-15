# 11. Is Subsequence
def is_subsequence(s, t):
    # Initialize a pointer to keep track of the current position in string t
    t_index = 0
    for char in s:
        # Move the pointer forward until we find a match or reach the end
        while t_index < len(t) and t[t_index] != char:
            t_index += 1
        
        # If we've reached the end of t without winding a match, return False
        if t_index == len(t):
            return False
        
        # Move the pointer forward to the next character in t
        t_index += 1
    
    return True
    
# Example usage:
s = "ace"
t = "abcde"
print(is_subsequence(s, t))

# # 10 Valid Parenthesis
# def is_valid(s):
#     # Initialize an empty stack to keep track of opening brackets
#     stack = []
    
#     # Define a mapping dictionary
#     mapping = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
    
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
            
#             if mapping[char] != top_element:
#                 return False
        
#         else:
#             stack.append(char)
    
#     # If the stack is empty, it means that all characters have been matched, so return True
#     return not stack

# # Example usage:
# s = "()[]{}"
# print(is_valid(s)) 

# a = "(]"
# print(is_valid(a))

# # 9. 
# from collections import Counter
# def check_permutation(s1, s2):
#     len_s1, len_s2 = len(s1), len(s2)
    
#     if len_s2 < len_s1:
#         return False
    
#     s1_counter = Counter(s1)
#     s2_counter = Counter(s2[:len_s1])
    
#     if s1_counter == s2_counter:
#         return True
    
#     for i in range(len_s1, len_s2):
#         s2_counter[s2[i]] += 1
        
#         if s2_counter[s2[i - len_s1]] == 1:
#             del s2_counter[s2[i - len_s1]]
#         else:
#             s2_counter[s2[i - len_s1]] -= 1
            
#         if s1_counter == s2_counter:
#             return True
    
#     return False


# # Example usage:
# s1 = "bao"
# s2 = "eidbaooo"
# result = check_permutation(s1, s2)
# print(result)

# # 8.
# def frequency_sort(s):
#     char_freq = {}
    
#     for char in s:
#         char_freq[char] = char_freq.get(char, 0) + 1
        
#     sorted_chars = sorted(char_freq.keys(), key=lambda x : char_freq[x], reverse=True)
    
#     sorted_string = ''
#     for char in sorted_chars:
#         sorted_string += char * char_freq[char]
    
    
#     return sorted_string


# # Example usage:
# s = "tree"
# result = frequency_sort(s)
# print(result)  


# # 7.
# def roman_to_int(s):
#     roman_map = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
    
#     total = 0
    
#     for i in range(len(s)):
#         if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
#             total -= roman_map[s[i]]
#         else:
#             total += roman_map[s[i]]
    
#     return total

# # Example usage:
# roman_numeral = "CDII"
# result = roman_to_int(roman_numeral)
# print(result)


# # 6.
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


# # 5.
# def group_anagrams(strs):
#     anagrams = {}
    
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
        
#         if sorted_word in anagrams:
#             anagrams[sorted_word].append(word)
#         else:
#             anagrams[sorted_word] = [word]
    
#     return list(anagrams.values())

# # Example usage:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = group_anagrams(strs)
# print(result)


# # 4.
# def character_replacement(s, k):
#     left = 0
#     char_count = {}
#     max_count = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         char_count[s[right]] = char_count.get(s[right], 0) + 1
        
#         max_count = max(max_count, char_count[s[right]])
        
#         if right - left + 1 - max_count > k:
#             char_count[s[left]] -= 1
#             left += 1
            
#         max_length = max(max_length, right - left + 1)
    
#     return max_length

# # Example usage:
# s = "AABABBA"
# k = 1
# result = character_replacement(s, k)
# print(result)


# # 3.
# from collections import Counter
# def min_window(s, t):
#     left, right = 0, 0
#     required_chars = Counter(t)
#     missing_chars = len(t)
#     min_len = len(s) + 1
#     min_window_substr = ''
    
#     while right < len(s):
#         if s[right] in required_chars:
#             required_chars[s[right]] -= 1
            
#             if required_chars[s[right]] >= 0:
#                 missing_chars -= 1
        
#         while missing_chars == 0:
#             if right - left + 1 < min_len:
#                 min_len = right - left + 1
#                 min_window_substr = s[left: right + 1]
                
#             if s[left] in required_chars:
#                 required_chars[s[left]] += 1
                
#                 if required_chars[s[left]] > 0:
#                     missing_chars += 1
            
#             left += 1
                
#         right += 1
    
#     return min_window_substr


# # Example usage:
# s = "ADOBECODEBANC"
# t = "ABC"
# result = min_window(s, t)
# print(result)


# # 2. 
# from collections import Counter
# def find_anagrams(s, p):
#     len_s, len_p = len(s), len(p)
#     result = []
    
#     if len_s < len_p:
#         return result
    
#     p_counter = Counter(p)
#     s_counter = Counter(s[:len_p])
    
#     if p_counter == s_counter:
#         result.append(0)
        
#     for i in range(len_p, len_s):
#         s_counter[s[i]] += 1
        
#         if s_counter[s[i - len_p]] == 1:
#             del s_counter[s[i - len_p]]
#         else:
#             s_counter[s[i - len_p]] -= 1
            
#         if p_counter == s_counter:
#             result.append(i - len_p + 1)
            
#     return result

# # example test
# s = "cbaebabacdcab"
# p = "abc"
# result = find_anagrams(s, p)
# print(result) 


# # 1.
# def reverse_string(s):
#     left, right = 0, len(s) - 1
    
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1
        
# # example test
# test_string = ['a', 'y', 'o', 'm', 'i', 'd', 'e']
# reverse_string(test_string)
# print(test_string)