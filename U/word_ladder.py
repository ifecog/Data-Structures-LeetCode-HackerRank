"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""

from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
        
    L = len(beginWord)
    
    # Build a dictionary where the key is a generic pattern of the word with one letter replaced by '*' and the value is a list of words from wordList that matches th pattern
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            all_combo_dict[pattern].append(word)
            
    # BFS Queue : (current_word, transformation_level)
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])
    
    while queue:
        current_word, level = queue.popleft()
        
        for i in range(L):
            pattern = current_word[:i] + '*' + current_word[i+1:]
            
            for neighbor in all_combo_dict[pattern]:
                if neighbor == endWord:
                    return level + 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
                    
            all_combo_dict[pattern] = []
            
    return 0
    
            
            
# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))