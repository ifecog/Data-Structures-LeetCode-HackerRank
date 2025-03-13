def find_words(board, words):
    m, n = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(i, j, k, word, visited):
        if k == len(word):
            return True
        
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k] or (i, j) in visited:
            return
        
        visited.add((i, j))
        
        for di, dj in directions:
            if dfs(i + di, j + dj, k + 1, word, visited.copy()):
                return True
            
        visited.remove((i, j))
        
        return False
    
    found_words = set()
    visited = set()
    
    for word in words:
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
                    break
                
    return list(found_words)

# Example usage
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(find_words(board, words))


# def exist(board, word):
#     m, n = len(board), len(board[0])
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     def dfs(i, j, k):
#         if k == len(word):
#             return True
        
#         if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
#             return 
        
#         temp, board[i][j] = board[i][j], None
        
#         for di, dj in directions:
#             if dfs(i + di, j + dj, k + 1):
#                 return True
            
#         board[i][j] = temp
        
#         return False
    
#     for i in range(m):
#         for j in range(n):
#             if dfs(i, j, 0):
#                 return True
            
#     return False

# # Example usage
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# print(exist(board, word))
    