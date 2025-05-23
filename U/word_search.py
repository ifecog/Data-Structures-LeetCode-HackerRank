# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
        
        
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
    
#     def insert(self, word):
#         node = self.root
        
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
                
#             node = node.children[char]
            
#         node.is_end = True
        
        
# def find_words(board, words):
#     m, n = len(board), len(board[0])
#     directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#     found_words = set()
    
#     # Build Trie for the word list
#     trie = Trie()
    
#     for word in words:
#         trie.insert(word)
        
#     def dfs(i, j, node, path):
#         if node.is_end:
#             found_words.add(path)
#             node.is_end = False # Aviod duplicate work
            
#         if not (0 <= i < m and 0 <= j < n) or board[i][j] not in node.children:
#             return
        
#         char = board[i][j]
#         next_node = node.children[char]
#         board[i][j] = '#'
        
#         for di, dj in directions:
#             ni, nj = i + di, j + dj
#             dfs(ni, nj, next_node, path + char)
            
#         board[i][j] = char
        
        
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] in trie.root.children:
#                 dfs(i, j, trie.root, '')
                
#     return list(found_words)
 
# # Example usage
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# print(find_words(board, words))       

# def find_words(board, words):
#     m, n = len(board), len(board[0])
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     def dfs(i, j, k, word, visited):
#         if k == len(word):
#             return True
        
#         if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k] or (i, j) in visited:
#             return
        
#         visited.add((i, j))
        
#         for di, dj in directions:
#             if dfs(i + di, j + dj, k + 1, word, visited.copy()):
#                 return True
            
#         visited.remove((i, j))
        
#         return False
    
#     found_words = set()
#     visited = set()
    
#     for word in words:
#         for i in range(m):
#             for j in range(n):
#                 if dfs(i, j, 0, word, visited):
#                     found_words.add(word)
#                     visited.clear()
#                     break
                
#     return list(found_words)




def exist(board, word):
    m, n = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(i, j, k):
        if k == len(word):
            return True
        
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
            return 
        
        temp, board[i][j] = board[i][j], None
        
        for di, dj in directions:
            if dfs(i + di, j + dj, k + 1):
                return True
            
        board[i][j] = temp
        
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
    