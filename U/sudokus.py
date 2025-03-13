def solve_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
                
            rows[i].add(num)
            cols[j].add(num)
            box_idx = (i // 3) * 3 + (j // 3)
            boxes[box_idx].add(num)
                
    def is_valid(i, j, num):
        box_idx = (i // 3) * 3 + (j // 3)
        
        return num not in rows[i] and num not in cols[j] and num not in boxes[box_idx]
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    
                    for num in map(str, range(1, 10)):
                        if is_valid(i, j, num):
                            board[i][j] = num
                            
                            rows[i].add(num)
                            cols[j].add(num)
                            box_idx = (i // 3) * 3 + (j // 3)
                            boxes[box_idx].add(num)
                            
                            if solve():
                                return True
                            
                            board[i][j] = '.'
                            rows[i].remove(num)
                            cols[j].remove(num)
                            box_idx = (i // 3) * 3 + (j // 3)
                            boxes[box_idx].remove(num)
                    
                    return False
        
        return True
    
    solve()
    
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


def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            
            if num == '.':
                continue
            
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            box_idx = (i // 3) * 3 + (j // 3)
            if num in boxes[box_idx]:
                return False
            boxes[box_idx].add(num)
            
    return True

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
print(is_valid_sudoku(board))   