def exist(board, word):
    # Define a nested funtion that performs DFS. It takes in 3 parameters... i & j are the coordinates of the current cell. j is the current index in the word string
    def dfs(i, j, k):
        if k == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
            return False
        
        
        temp = board[i][j]
        board[i][j] = '#'
        
        # Explore neighboring cells (up, left, down, right). It there is a successful DFS (i.e. the word is found), return True
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(i + x, j + y, k + 1):
                return True
        
        board[i][j] = temp
        
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True
    
    return False

# Example usage
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))

