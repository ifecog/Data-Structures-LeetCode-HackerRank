"""
Given a sentence, need to calculate the absolute difference of vowels and consonants for each word and return a list of strings sorted in the context of whose difference is the lowest. If two words have same difference, return the lexicographically smaller one first.
"""

def count_vowels_and_consonants(word):
    vowels = set('aeiouAEIOU')
    vowel_count, consonant_count = 0, 0
    
    for char in word:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
            
    return vowel_count, consonant_count


def sort_words_by_difference(sentence):
    words = sentence.split()
    word_diffences = []
    
    for word in words:
        vowel_count, consonant_count = count_vowels_and_consonants(word)
        difference = abs(vowel_count - consonant_count)
        word_diffences.append((difference, word))
        
    # Sort by difference and then lexicographically
    word_diffences.sort(key=lambda x: (x[0], x[1]))
    
    sorted_words = [word for _, word in word_diffences]
    
    return sorted_words

# Example usage
sentence = "hello world this is a test"
result = sort_words_by_difference(sentence)
print(result)