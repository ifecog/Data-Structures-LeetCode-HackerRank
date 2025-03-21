def longest_repeating_character_replacement(s, k):
    """You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Args:
        s (str): a string of characters
        k (int): an integer representing the number of times for replacement
    """

    # This is solved using the sliding window approach
    char_count = {}
    left, max_count, max_length = 0, 0, 0
    
    for right in range(len(s)):
        # Increment the count for the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update the maximum count to the highest count of any character in the window
        max_count = max(max_count, char_count[s[right]])
        
        # If the number of characters that need to be replaced is more than k, shrink the window from the left
        if right - left + 1 - max_count > k:
            char_count[s[left]] -= 1
            left += 1
            
        # Update the maxlength of the curernt window
        max_length = max(max_length, right - left + 1)
    
    return max_length
           
    
# Example usage:
s = "AABABBA"
k = 1
result = longest_repeating_character_replacement(s, k)
print(result)