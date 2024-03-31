def remove_anagrams(words):
    """You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

    In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

    Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

    Args:
        words (string): an array of words
    """
    

    non_anagrams = []
    
    for i, word in enumerate(words):
        if i == 0 or sorted(word) != sorted(words[i - 1]):
            non_anagrams.append(word)
    
    return non_anagrams




    # initialize an empty list to store the non_anagram words
    # non_anagrams = []
    
    # for i, word in enumerate(words):
    #     if i == 0 or sorted(word) != sorted(words[i - 1]):
    #         non_anagrams.append(word)
    
    # return non_anagrams

# Example usage:
words = ["dacb", "abdc", "abc", "cba"]
result = remove_anagrams(words)
print(result)