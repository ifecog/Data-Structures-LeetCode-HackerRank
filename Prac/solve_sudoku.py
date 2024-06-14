def solve_sudoku(board):
    # Helper function to check of the board is valid
    def is_valid(board, r, c, num):
        # Check rows
        for i in range(9):
            if board[r][i] == num:
                return False
        
        # Check columns
        for i in range(9):
            if board[i][c] == num:
                return False
            
        # Check the 3x3 sub-boxes
        box_r, box_c = (r // 3) * 3, (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_r + i][box_c + j] == num:
                    return False
        
        return True
    
    
    # Helper function to solve sudoku (Replace '.' with numbers)
    def solve(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if solve(board):
                                return True
                            board[r][c] = '.'
                    
                    return False
        
        return True
    
    solve(board)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solve_sudoku(board)
for row in board:
    print(row)