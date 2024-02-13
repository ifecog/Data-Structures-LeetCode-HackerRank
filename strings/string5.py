def group_anagrams(strs):
    anagrams = {}
        
    for word in strs:
        sorted_words = ''.join(sorted(word))
            
        if sorted_words in anagrams:
            anagrams[sorted_words].append(word)
        else:
            anagrams[sorted_words] = [word]
                
    return list(anagrams.values())


# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)
