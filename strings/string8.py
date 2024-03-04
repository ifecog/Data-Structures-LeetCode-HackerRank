def frequency_sort(s):
    """Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.

    Args:
        s (string): a string of characters
    """
    
    char_freq = {}
    
    for char in s:
        # count the frequency of each character in the string
        char_freq[char] = char_freq.get(char, 0) + 1
        
    # sort the characters based on their frequencies in decreasing order
    sorted_chars = sorted(char_freq.keys(), key=lambda x : char_freq[x], reverse=True)
    
    # construct the sorted string
    sorted_string = ''
    for char in sorted_chars:
        sorted_string += char * char_freq[char]
    
    return sorted_string

# Example usage:
s = "tree"
result = frequency_sort(s)
print(result)  