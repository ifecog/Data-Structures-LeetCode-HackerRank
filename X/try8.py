def exist(board, word):
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    
    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once.

    Args:
        board (list[list[str]]): an m x n grid of characters board
        word (str): a word to be searched in the grid
    """

    def dfs(i, j, k):
        # If we have matched all characters in the word, return True
        if k == len(word):
            return True

        # If the indices are out of bounds or the current cell does not match the character in the word, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        # Temporarily mark the current cell as visited by storing the current value and setting it to None
        temp, board[i][j] = board[i][j], None

        # Explore all 4 possible directions: right, down, left, and up
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(i + x, j + y, k + 1):
                return True

        # Restore the current cell's value before returning False
        board[i][j] = temp
        return False
    
    # Iterate through each cell in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Start the DFS from the current cell if it matches the first character in the word
            if dfs(i, j, 0):
                return True

    # Return False if no path is found that matches the word
    return False

# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))  # Output should be True
