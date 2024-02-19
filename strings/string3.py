from collections import Counter


def min_window(s, t):
    """Given 2 strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return an empty string ''.

    Args:
        s (string): a string of characters
        t (string): a string of characters
    """
    
    # initiate pointers
    left, right = 0, 0
    # initiate variables
    min_len = len(s) + 1
    min_window_substr = ''
    required_chars = Counter(t)
    missing_chars = len(t)
    
    while right < len(s):
        if s[right] in required_chars:
            required_chars[s[right]] -= 1
            
            if required_chars[s[right]] >= 0:
                missing_chars -= 1
                
        while missing_chars == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_substr = s[left:right + 1]
                
            if s[left] in required_chars:
                required_chars[s[left]] += 1
                
                if required_chars[s[left]] > 0:
                    missing_chars += 1
            
            left += 1
        
        right += 1
    
    return min_window_substr


# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
result = min_window(s, t)
print(result)