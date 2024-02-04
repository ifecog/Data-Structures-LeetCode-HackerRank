def character_replacement(s, k):
    """You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Args:
        s (str): a string of characters
        k (int): an integer representing the number of times for replacement
    """
    
    # initialize variables
    max_length = 0
    max_count = 0
    char_count = {}
    left = 0
    
    for right in range(len(s)):
        # increment the count of the character at the right pointer
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # update the maximum count
        max_count = max(max_count, char_count[s[right]])
        
        # check if the current window needs shrinking
        if right - left + 1 - max_count > k:
            char_count[s[left]] -= 1
            left += 1
            
        # update maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
s = "AABABBA"
k = 1
result = character_replacement(s, k)
print(result)