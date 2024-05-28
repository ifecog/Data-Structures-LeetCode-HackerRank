# def find_words(board, words):
#     """Given an m x n board of characters and a list of strings words, return all words on the board.

#     Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

#     Args:
#         board (grid): an m x n grid of characters board
#         words (list): a list of words
#     """
    
#     def dfs(i, j, k, word):
#         if k == len(word):
#             return word
        
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
#             return None
        
#         temp = board[i][j]
#         board[i][j] = '#'
        
#         for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             res = dfs(i + x, j + y, k + 1, word)
#             if res:
#                 return res
        
#         board[i][j] = temp
#         return None
    
    
#     res = set()  # Use a set to store unique words
#     for word in words:
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 found_word = dfs(i, j, 0, word)
#                 if found_word:
#                     res.add(found_word)  # Add only unique words to the set
    
#     return list(res)

def find_words(board, words):
    def dfs(i, j, k, word, visited):
        if k == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board [i][j] != word[k] or (i, j) in visited:
            return False

        visited.add((i, j))  # Mark current cell as visited

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(i + x, j + y, k + 1, word, visited.copy()):
                return True

        visited.remove((i, j))  # Unmark cell before backtracking

        return False
    visited = set()
    found_words = set()
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
    
    return list(found_words)

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))