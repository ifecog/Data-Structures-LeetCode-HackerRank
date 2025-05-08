"""Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word"""
    

def fullJustify(words, maxWidth):
    n = len(words)
    i = 0 # Pointer to track the current word
    result = []
    
    while i < n:
        line_len = len(words[i]) # Length of the 1st word in the line
        j = i + 1 # Pointer to explore how mny words fit
        
        # Try to fit as many words as possible in the current line
        while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
            line_len += len(words[j]) # Add next word length
            j += 1 # Move to the next word
            
            # Now, words from i to j - 1 fit in this line
            
        # Build the line with the justified text
        line = ''
        number_of_words = j - i
            
        # If it is the last line or only one word, left-justify
        if j == n or number_of_words == 1:
            line = ' '.join(words[i:j])
            line += ' ' * (maxWidth - len(line)) # Fill the rest with spaces
        
        else:
            total_spaces = maxWidth - line_len
            space_between_words = total_spaces // (number_of_words - 1)
            extra_spaces = total_spaces % (number_of_words - 1)
            
            # Distribute spaces
            for k in range(i, j - 1):
                line += words[k]
                
                # Add base spaces + 1 extra if needed
                line += ' ' * (space_between_words + (1 if k - i < extra_spaces else 0))
            
            line += words[j - 1] # Add the last word
        
        result.append(line)
        i = j
        
    return result    
            
            
        
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
for line in fullJustify(words, maxWidth):
    print(f'"{line}"')

        
        
"""📈 Time and Space Complexity:
Time Complexity: O(N * M)

N = number of words

M = average word length

Because we touch each word and each character at most once.

Space Complexity: O(N * M)

We build the final list of strings and use some temporary space."""