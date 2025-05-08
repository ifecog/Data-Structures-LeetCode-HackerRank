# def solve_sudoku(board):
    # def is_valid_sudoku(board):
    #     rows = [set() for _ in range(9)]
    #     cols = [set() for _ in range(9)]
    #     boxes = [set() for _ in range(9)]
        
    #     for i in range(9):
    #         for j in range(9):
    #             num = board[i][j]
    #             if num == '.':
    #                 continue
                
    #             if num in rows[i]:
    #                 return False
    #             rows[i].add(num)

    #             if num in cols[j]:
    #                 return False
    #             cols[j].add(num)
                
    #             box_index = ((i // 3) * 3) + (j // 3)
    #             if num in boxes[box_index]:
    #                 return False
    #             boxes[box_index].add(num)
        
    #     return True
    
    # for i in range(9):
    #     for j in range(9):            
    #         if board[i][j] == '.':
                
    #             for num in map(str, range(1, 10)):
    #                 board[i][j] = num

    #                 if is_valid_sudoku(board):                    
    #                     if solve_sudoku(board):
    #                         return True
                    
    #                 board[i][j] = '.'
                    
    #             return False
            
    # return True   



def solve_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                
                rows[i].add(num)
                cols[j].add(num)
                box_index = ((i // 3) * 3) + (j // 3)
                boxes[box_index].add(num)
                
    def is_valid(i, j, num):
        box_index = ((i // 3) * 3) + (j // 3)
        return num not in rows[i] and num not in cols[j] and num not in boxes[box_index]
    
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    
                    for num in map(str, range(1, 10)):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            
                            rows[i].add(num)
                            cols[j].add(num)
                            boxes[((i // 3) * 3) + (j // 3)].add(num)
                            
                            if solve():
                                return True
                            
                            # Undo the move
                            board[i][j] = '.'
                            
                            rows[i].remove(num)
                            cols[j].remove(num)
                            boxes[((i // 3) * 3) + (j // 3)].remove(num)
                        
                    return False
        
        return True
    
    solve()


# board = [
#     [".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]
# ]

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