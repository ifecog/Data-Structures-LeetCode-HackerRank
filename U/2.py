def count_vowels_and_consonants(word):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

def sort_words_by_difference(sentence):
    words = sentence.split()
    word_differences = []
    
    for word in words:
        vowel_count, consonant_count = count_vowels_and_consonants(word)
        difference = abs(vowel_count - consonant_count)
        word_differences.append((difference, word))
    
    # Sort by difference, then lexicographically
    word_differences.sort(key=lambda x: (x[0], x[1]))
    
    # Extract the sorted words
    sorted_words = [word for _, word in word_differences]
    return sorted_words


sentence = "hello world this is a test"
result = sort_words_by_difference(sentence)
print(result)