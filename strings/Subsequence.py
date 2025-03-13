def is_subsequence(s, t):
    """Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Args:
        s (str): A string of characters
        t (str): A string of characters
    """
    
    # Initialize a pointer to keep track of the current position in string t
    t_index = 0
    
    # Iterate over each character in string s
    for char in s:
        # Move the pointer forward in string t until we find a match or reach the end
        while t_index < len(t) and t[t_index] != char:
            t_index += 1
        
        # If we reach the end of string t without finding a match, return False
        if t_index == len(t):
            return False
        
        # Move the pointer forward to the next character in t
        t_index += 1
    
    return True

# Example usage:
s = "ace"
t = "abcde"
print(len(t))
print(is_subsequence(s, t))