directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def exist(board, word):
    """Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

    Args:
        board (grid): an m x n grid of characters board
        word (string): a word
    """
    m, n = len(board), len(board[0])

    def dfs(i, j, k):
        # If we have matched all characters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bounds or the current cell does not match the character in the word, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        # Temporarily mark the current cell as visited by storing the current value and setting it to None
        temp, board[i][j] = board[i][j], None
        
        # Explore all 4 possible directions (right, left, up, down)
        for dx, dy in directions:
            if dfs(i + dx, j + dy, k + 1):
                return True

        # Restore the current cell's value
        board[i][j] = temp
        
        return False
    
    for x in range(m):
        for y in range(n):
            # Start DFS from the current cell if it matches the first character in the word
            if dfs(x, y, 0):
                return True
    
    return False
    

# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))