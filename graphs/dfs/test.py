# Word Search II
directions = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

def find_words(board, words):
    m, n = len(board), len(board[0])
    
    def dfs(x, y, z, word, visited):
        # If we have matched all the characters in the word, return True
        if z == len(word):
            return True
        
        # If the indices are out of bounds and the current cell does not match any character in the word and the cell is already visited, return False
        if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != word[z] or (x, y) in visited:
            return False
        
        # Add the current cell to the visited set
        visited.add((x, y))
        
        for dx, dy in directions:
            if dfs(x + dx, y + dy, z + 1, word, visited):
                return True
        
        visited.remove((x, y))
        
        return False
    
    visited = set()
    found_words = set()
    
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


# # Word Search I
# directions = [
#     (0, 1), (0, -1), (1, 0), (-1, 0)
# ]

# def exist(board, word):
#     m, n = len(board), len(board[0])
    
#     def dfs(x, y, z):
#         # If we have matshed all the characters in the word, return True
#         if z == len(word):
#             return True
        
#         # If the indices are withing the boundary and the current cell does not match eny character in the word, return False
#         if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != word[z]:
#             return False
        
#         # Temporarily mark the current cell as visited
#         temp, board[x][y] = board[x][y], None
        
#         for dx, dy in directions:
#             if dfs(x + dx, y + dy, z + 1):
#                 return True
            
#         board[x][y] = temp
        
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

# # Number of Islands
# def num_islands(grid):
#     island_count = 0
    
#     def dfs(r, c):
#         if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
#             return
        
#         grid[r][c] = '0'
        
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)
        
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 island_count += 1
#                 dfs(i, j)
        
#     return island_count

# grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# print(num_islands(grid))


# # Flood Fill
# def flood_fill(image, sr, sc, color):
#     # Get the original color of the starting image
#     original_color = image[sr][sc]
    
#     if original_color == color:
#         return image
    
#     def dfs(r, c):
#         if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
#             return
        
#         if image[r][c] == original_color:
#             image[r][c] = color
            
#             dfs(r + 1, c)
#             dfs(r - 1, c)
#             dfs(r, c + 1)
#             dfs(r, c - 1)
    
#     dfs(sr, sc)
    
#     return image

# # Example usage
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# color = 2

# print(flood_fill(image, sr, sc, color))


# # Calculate Equation
# from collections import defaultdict

# def calc_equation(equations, values, queries):
#     # Build the graph
#     graph = defaultdict(dict)
#     for (a, b), value in zip(equations, values):
#         graph[a][b] = value
#         graph[b][a] = 1/value
        
#     def dfs(start, end, visited):
#         if start not in graph or end not in graph:
#             return -1.0
        
#         if start == end:
#             return 1.0
        
#         # Mark the start node as visited
#         visited.add(start)
        
#         # Explore all neighbors of the start node
#         for neighbor in graph[start]:
#             if neighbor in visited:
#                 continue
            
#             # Recursively explore the neighbor node
#             temp = dfs(neighbor, end, visited)
#             if temp != -1.0:
#                 return temp * graph[start][neighbor]
        
#         return -1.0
    
#     return [dfs(c, d, set()) if c in graph and d in graph else -1.0 for c, d in queries]
    
# # Example usage
# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# print(calc_equation(equations, values, queries))