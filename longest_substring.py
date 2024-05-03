def length_of_longest_substring(s):
    """Given a string s, find the length of the longest 
    substring without repeating characters.

    Args:
        s (string): a string of characters

    Returns:
        int: length of the longest substring without repeating characters
    """
    """
    Solution:
    
    Initialize max_length to 0, start to 0, and char_index_map to an empty dictionary. The char_index_map will store the most recent index of each character encountered.

    Iterate through the string s using a sliding window defined by start and end.
    
    If the character at index end is already in char_index_map and its index is greater than or equal to start, it means the character is repeating within the current window. In this case, update start to the index after the last occurrence of the repeating character.
    
    Update the index of the current character in char_index_map.
    
    Update max_length by taking the maximum of its current value and the length of the current substring.
    
    Finally, return max_length, which represents the length of the longest substring without repeating characters.
    
    """
    
    char_index_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If the character in the right index is already in the char_count dict and its index is greater than or equal to 'left', it means that the character is repeating. Hence, update start to the index after the last occurence of the repeating character.
        if s[right] in char_index_map and char_index_map[s[right]] >= left:
            left = char_index_map[s[right]] + 1
        
        char_index_map[s[right]] = right
        max_length = max(max_length, right - left + 1)  
    
    return max_length

s = "abcabcbb"
print(length_of_longest_substring(s))