def find_words(board, words):
    """
    Given an m x n grid of characters board and a list of strings words, return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once in a word.

    Args:
        board (list[list[str]]): an m x n grid of characters.
        words (list[str]): a list of words to search for in the board.
    
    Returns:
        list[str]: a list of words found in the board.
    """
    
    def dfs(i, j, k, word, visited):
        # If we have matched all the characters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bound or the current word does not match the character in the word, or the cell is already visited, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k] or (i, j) in visited:
            return False
        
        # Mark the current cell as visited
        visited.add((i, j))
        
        # Recursively explore the 4 possible directions (right, left, up, down)
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(x + i, y + j, k + 1, word, visited.copy()):
                return True
            
        # Remove the current cell from visited
        visited.remove((i, j))
        
        return False
    
    visited = set()
    found_words = set()
    
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
                    break
    
    return list(found_words)
    

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))