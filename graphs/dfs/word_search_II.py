directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def find_words(board, words):
    m, n = len(board), len(board[0])
    
    # DFS function to find the words in the board
    def dfs(i, j, k, word, visited):
        # If we have matched all the characters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bound or the current cell does not match the character in the word or the cell is already visited, return False
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k] or (i, j) in visited:
            return False
        
        # Add the current cell to the visited set
        visited.add((i, j))
        
        # Explore all 4 directions
        for dx, dy in directions:
            if dfs(i + dx, j + dy, k + 1, word, visited.copy()):
                return True
            
        # Remove the current cell from the visited set
        visited.remove((i, j))
        
        return False
    
    visited = set()
    found_words = set()
    
    for word in words:
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
                    break
    
    return list(found_words)

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))