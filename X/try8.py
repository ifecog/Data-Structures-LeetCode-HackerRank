def find_words(board, words):
    # This is solved using the depth first search approach
    def dfs(i, j, k, word, visited):
        # If we have matched all characters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bound or the current cell does not martch the character in the word or the cell is already visited, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k] or (i, j) in visited:
            return False
        
        # Temporatily mark the cell as visited
        visited.add((i, j))
        
        # Explore adjacent cells
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(x + i, y + j, k + 1, word, visited.copy()):
                return True
            
        # Remoce the current cell from the visited set
        visited.remove((i, j))
        
        return False
    
    visited = set()
    found_words = set()
    
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Perform DFS startin from the first cell
                if dfs(i, j, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
                    break
    
    return list(found_words)


# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))