def countBattleships(board):
    if not board:
        return 0
    
    m, n = len(board), len(board[0])
    count = 0
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                continue
            
            # Check if it is the start of a new battleship
            if i > 0 and board[i - 1][j] == 'X':
                continue
            if j > 0 and board[i][j - 1] == 'X':
                continue
            
            count += 1
            
    return count


board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
print(countBattleships(board))