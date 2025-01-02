from collections import Counter

def check_permutation(s1, s2):
    """Given 2 strings s1 and s2, return true of s2 contains a permutation of s1, or False otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.

    Args:
        s1 (string): a string of characters
        s2 (string): a string of characters
    """
    
    len_s1, len_s2 = len(s1), len(s2)
    
    if len_s2 < len_s1:
        return False
    
    s1_counter = Counter(s1)
    s2_counter = Counter(s2[:len_s1])
    
    if s1_counter == s2_counter:
        return True
    
    for i in range(len_s1, len_s2):
        s2_counter[s2[i]] += 1
        
        if s2_counter[s2[i - len_s1]] == 1:
            del s2_counter[s2[i - len_s1]]
        else:
            s2_counter[s2[i - len_s1]] -= 1
            
        if s1_counter == s2_counter:
            return True
    
    return False
        
# Example usage:
s1 = "auy"
s2 = "eidbaooo"
result = check_permutation(s1, s2)
print(result)