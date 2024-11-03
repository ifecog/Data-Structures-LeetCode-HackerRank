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
    
    # DFS helper Function to find words in the board
    def dfs(x, y, z):
        # If we have matched all the characters in the word, return True
        if z == len(word):
            return True
        
        # If the indices are out of bounds of the current cell and do not match any charater in the word, return False
        if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != word[z]:
            return False
        
        # Temporarily mark the current cell as visited
        temp, board[x][y] = board[x][y], None
        
        # Explore all 4 possible directions
        for dx, dy in directions:
            if dfs(x + dx, y + dy, z + 1):
                return True
        
        # Restore the current cell's value
        board[x][y] = temp
        
        return False
    
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    
    return False

# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))