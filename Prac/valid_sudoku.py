def is_valid_sudoku(board):
    # Use sets to keep track of seen numbers in rows, columns, and sub-boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue
            
            # Check row
            if num in rows[i]:
                return False
            rows[i].add(num)
            
            # Check col
            if num in cols[j]:
                return False
            cols[j].add(num)
            
            # Check 3x3 sub-box
            box_index = (i // 3) * 3 + (j // 3)

            if num in boxes[box_index]:
                return False
            boxes[box_index].add(num)
            
    return True


# Example usage:
# sol = Solution()
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