def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())
    
    
# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)


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

# from collections import Counter

# def find_anagrams(s, p):
#     result = []
    
#     len_s, len_p = len(s), len(p)
#     if len_s < len_p:
#         return result
    
#     # Counters
#     p_counter = Counter(p)
#     window_counter = Counter(s[:len_p])
    
#     # Check if the first window is an anagram
#     if p_counter == window_counter:
#         result.append(0)
    
#     # Slide the window through the rest of s
#     for i in range(len_p, len_s):
#         window_counter[s[i]] += 1
        
#         # Remove the leftmost element from the current window
#         if window_counter[s[i - len_p]] == 1:
#             del window_counter[s[i - len_p]]
#         else:
#             window_counter[s[i - len_p]] -= 1
        
#         if window_counter == p_counter:
#             result.append(i - len_p + 1)    
    
#     return result

# # Example usage
# s = "cbaebabacdcab"
# p = "abc"
# result = find_anagrams(s, p)
# print(result) 

# def are_anagrams(s1, s2):
#     # sorted_s1 = ''.join(sorted(s1))
#     # sorted_s2 = ''.join(sorted(s2)) 
    
#     # return sorted_s1 == sorted_s2
    
#     return sorted(s1) == sorted(s2)
        

# # Example usage:
# a = 'george'
# b = 'rogege'
# print(are_anagrams(a, b))