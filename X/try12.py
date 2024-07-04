def character_replacement(s, k):
    # This is solved using the slidin window approach
    char_count = {}
    left = 0
    max_count = 0
    max_length = 0
    
    for right in range(len(s)):
        # Increment the count for the current character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update the max count to the hihest count of any character in the window
        max_count = max(max_count, char_count[s[right]])
        
        # If the current window size minus the max_count character is greater than k, it means that we need more than k replacements to make all the characters the same.
        # a. decrement the characters in the left pointer
        # b. shrink the window from the left by incrementing the left pointer
        if right - left + 1 - max_count > k:
            char_count[s[left]] -= 1
            left += 1
        
        # Update the length of longest substring
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
s = "AABABBA"
k = 1
result = character_replacement(s, k)
print(result)