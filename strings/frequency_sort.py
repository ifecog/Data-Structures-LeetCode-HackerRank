from collections import Counter

def frequency_sort(s):
    """Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string. Return the sorted string. If there are multiple answers, return any of them.

    Args:
        s (string): a string of characters
    """
    
    # sorted_str = ''
    # char_freq = {}
    
    # for char in s:
    #     # Count the frequency of each character in s
    #     char_freq[char] = char_freq.get(char, 0) + 1
        
    # sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    
    # for char in sorted_chars:
    #     sorted_str += char * char_freq[char]
    
    # return sorted_str
    
    char_freq = Counter(s)
    
    sorted_chars = sorted(char_freq.keys(), key=lambda i: char_freq[i], reverse=True)
    
    return ''.join(char * char_freq[char] for char in sorted_chars)
    
# Example usage:
s = "tree"
result = frequency_sort(s)
print(result)  