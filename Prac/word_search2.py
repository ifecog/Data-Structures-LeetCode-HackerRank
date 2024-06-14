def find_words(board, words):
    def dfs(i, j, k, word, visited):
        if k == len(word):
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board [i][j] != word[k] or (i, j) in visited:
            return False

        visited.add((i, j))

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(i + x, j + y, k + 1, word, visited.copy()):
                return True

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
    
    return list(found_words)

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))