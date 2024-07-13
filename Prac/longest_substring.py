def length_of_longest_substring(s):
    """Given a string s, find the length of the longest 
    substring without repeating characters.

    Args:
        s (string): a string of characters

    Returns:
        int: length of the longest substring without repeating characters
    """
    
    # This is solved using the sliding window approach
    
    # # 1. Using Set
    # char_set = set()
    # left = 0
    # max_length = 0
    
    # # Iterate using the sliding window approach
    # for right in range(len(s)):
    #     # If the character is already in the set, remove elements from the left
    #     while s[right] in char_set:
    #         char_set.remove(s[left])
    #         left += 1
        
    #     # Add the current character to the set
    #     char_set.add(s[right])
        
    #     # Update the maximum length
    #     max_length = max(max_length, right - left + 1)
    
    # return max_length
    
    # 2. Using dict
    char_index_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If the current char is already in the dict, move left pointer one place to the right
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        
        # Add the current char to the dict
        char_index_map[s[right]] = right
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length
    
# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))