from collections import Counter

def min_window(s, t):
    """
    Given 2 strings s and t of lengths m and n respectively, return the minimum window substring of s such that 
    every character in t (including duplicates) is included in the window. If there is no such substring, return an empty string ''.

    Args:
        s (str): a string of characters
        t (str): a string of characters
    """
    # Initialize pointers for the sliding window
    left, right = 0, 0
    
    # Initialize variables to track the minimum length of the window and the resulting substring
    min_len = len(s) + 1
    min_window_substr = ''
    
    # Counter for characters in t and the number of missing characters to form a valid window
    required_chars = Counter(t)
    missing_chars = len(t)
    
    # Start expanding the window with the right pointer
    while right < len(s):
        # If the character at the right pointer is in t, decrease its count in required_chars
        if s[right] in required_chars:
            required_chars[s[right]] -= 1
            
            # If the count is non-negative, it means we are still in need of this character
            if required_chars[s[right]] >= 0:
                missing_chars -= 1
        
        # When all characters are matched (missing_chars == 0), try to shrink the window from the left
        while missing_chars == 0:
            # Update the minimum window if the current one is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_substr = s[left:right + 1]
            
            # If the character at the left pointer is in t, increase its count in required_chars
            if s[left] in required_chars:
                required_chars[s[left]] += 1
                
                # If the count becomes positive, we are missing this character again
                if required_chars[s[left]] > 0:
                    missing_chars += 1
            
            # Move the left pointer to the right to shrink the window
            left += 1
        
        # Move the right pointer to the right to expand the window
        right += 1
    
    return min_window_substr

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)  # Expected output: "BANC"
