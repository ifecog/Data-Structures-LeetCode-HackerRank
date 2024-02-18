def group_anagrams(strs):
    """Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Args:
        strs (string): an array of strings
    """
    
    anagrams = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())


# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
