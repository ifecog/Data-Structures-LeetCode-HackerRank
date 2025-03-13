from collections import defaultdict

def numMatchingSubseq(s, words):
    waiting = defaultdict(list)
    
    # Initialize the waiting list with iterators for each word
    for word in words:
        waiting[word[0]].append(iter(word[1:]))
        
    count = 0
    for char in s:
        current_waiting = waiting[char]
        waiting[char] = []
        
        for it in current_waiting:
            next_char = next(it, None)
            
            if next_char is None:
                count += 1
            else:
                waiting[next_char].append(it)
                
    return count


# Example usage
s = "abcde"
words = ["a", "bb", "acd", "ace"]
print("Number of matching subsequences:", numMatchingSubseq(s, words))