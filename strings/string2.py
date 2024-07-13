from collections import Counter


def find_anagrams(s, p):
    """given 2 strings s and p, return an array of all the start indices of p's anagrams in s

    Args:
        s (string): a string variable
        p (_type_): a string variable
    """
    
    # This is solved using the sliding window approach
    
    result = []
    
    len_s, len_p = len(s), len(p)
    if len_s < len_p:
        return result
    
    # Count the occurence of characters in p
    p_counter = Counter(p)
    
    # Initialize the sliding window counter for the fordt window
    window_counter = Counter(s[:len_p])
    
    # Check if the first window is an anagram
    if window_counter == p_counter:
        result.append(0)
        
    # Slide the window through the rest of s
    for i in range(len_p, len_s):
        window_counter[s[i]] += 1
        
        # Remove the leftmost element after sliding
        if window_counter[s[i - len_p]] == 1:
            del window_counter[s[i - len_p]]
        else:
            window_counter[s[i - len_p]] -= 1
            
        # check if current window is an anagram
        if window_counter == p_counter:
            result.append(i - len_p + 1)
            
    return result



# example test
s = "cbaebabacdcab"
p = "abc"
result = find_anagrams(s, p)
print(result) 
