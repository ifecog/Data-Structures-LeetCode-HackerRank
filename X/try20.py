def length_of_longest_substring(s):
    # This is solved using the slidign window approach and the set data structure
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If the character is already in the set, remove elements from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the right character to the set
        char_set.add(s[right])
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length
    
    
# def length_of_longest_substring(s):
#     # This is solved using the sliding window approach and the dictionary data structure
#     char_index_map = {}
#     left = 0
#     max_length = 0
    
#     for right in range(len(s)):
#         # If the current character is already in the dictionary, move the left pointer one place to the right
#         if s[right] in char_index_map and char_index_map[s[right]] >= left:
#             left = char_index_map[s[right]] + 1
        
#         # Add the current character to the dictionary
#         char_index_map[s[right]] = right
        
#         max_length = max(max_length, right - left + 1)
    
#     return max_length
    

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))

