def exist(board, word):
    # This is sloved using the depth-forst-search approach (DFS)
    def dfs(i, j, k):
        # If we've matched all the charaters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bound or the current cell does not match the character in the word, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        # Temporarily mark the current cell as visited
        temp, board[i][j] = board[i][j], None
        
        # Explore adjacent cells
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(x + i, y + j, k + 1):
                return True
        
        # Restore the current cell's value
        board[i][j] = temp
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Perform DFS starting from the first cell
            if dfs(i, j, 0):
                return True
    
    return False


# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))  # Output should be True
