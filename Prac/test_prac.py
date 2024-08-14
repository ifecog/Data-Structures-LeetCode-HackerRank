def find_words(board, words):
    def dfs(i, j, k, word, visited):
        # If we have matched all the characters in the word, return True
        if k == len(word):
            return True
        
        # If the indices are out of bound or the current word does not match the character in the word, or the cell is already visited, return False
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k] or (i, j) in visited:
            return False
        
        # Mark the current cell as visited
        visited.add((i, j))
        
        # Explore all 4 possible directions (right, left, up, down)
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if dfs(x + i, y + j, k + 1, word, visited.copy()):
                return True
            
        # Remove current cell from visited set
        visited.remove((i, j))
        
        return False
    
    visited = set()
    found_words = set()
    
    for word in words:
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Perform DFS starting from the first cell
                if dfs(i, j, 0, word, visited):
                    found_words.add(word)
                    visited.clear()
                    break
    
    return list(found_words)
    


# def exist(board, word):
#     def dfs(i, j, k):
#         # IF we have matched all the characters in the word, return True
#         if k == len(word):
#             return True
        
#         # If the indices are out of bound or the current word does not match the character in the word, return False
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
#             return False
        
#         # Temporarily mark the current cell as visited by storing the current value and setting it to None
#         temp, board[i][j] = board[i][j], None
        
#         # Explore all 4 possible directions(right, left, up, down)
#         for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#             if dfs(i + x, j + y, k + 1):
#                 return True

#         # Restore the current cell's value
#         board[i][j] = temp
        
#         return False
    
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if dfs(i, j, 0):
#                 return True
            
#     return False
            


# def solve_sudoku(board):
#     # Helper function to check board validity
#     def is_valid(board, r, c, num):
#         # Check rows
#         for i in range(9):
#             if board[r][i] == num:
#                 return False
        
#         # Check cols
#         for i in range(9):
#             if board[i][c] == num:
#                 return False
            
#         # Check 3x3 sub-boxes
#         box_r, box_c = (r // 3) * 3, (c // 3) * 3
#         for i in range(3):
#             for j in range(3):
#                 if board[box_r + i][box_c + j] == num:
#                     return False
        
#         return True

    
#     # Helper function to solve the sudoku
#     def solve(board):
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     for num in '123456789':
#                         if is_valid(board, r, c, num):
#                             board[r][c] = num
#                             if solve(board):
#                                 return True
#                             board[r][c] = '.'
                    
#                     return False
        
#         return True
    
#     solve(board)

# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# solve_sudoku(board)
# for row in board:
#     print(row)

# def is_valid_sudoku(board):
#     # Use sets to keep track of seen numbers in rows, cols, and sub-boxes
#     rows = [set() for _ in range(9)]
#     cols = [set() for _ in range(9)]
#     boxes = [set() for _ in range(9)]
    
#     for i in range(9):
#         for j in range(9):
#             num = board[i][j]
#             if num == '.':
#                 continue
            
#             # Check row
#             if num in rows[i]:
#                 return False
#             rows[i].add(num)
            
#             # Check col
#             if num in cols[j]:
#                 return False
#             cols[j].add(num)
            
#             # Check 3x3 sub-box
#             box_index = (i // 3) * 3 + (j // 3)
            
#             if num in boxes[box_index]:
#                 return False
#             boxes[box_index].add(num)
            
#     return True
    
    
# # Example usage:
# # sol = Solution()
# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# print(is_valid_sudoku(board))            