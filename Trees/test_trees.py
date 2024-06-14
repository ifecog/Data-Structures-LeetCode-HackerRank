class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def kth_smallest(root, k):
    # Initialze an empty stack to store nodes for traversals
    stack = []
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        
        root = root.right
    
    return -1
        
# # Example usage:
# # Construct a binary search tree: [3,1,4,null,2]
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)

# k = 2
# print(kth_smallest(root, k))

# def right_side_view(root):
#     if not root:
#         return []
    
#     result = []
#     queue = [root]
    
#     while queue:
#         level_length = len(queue)
        
#         for i in range(level_length):
#             node = queue.pop(0)
            
#             if i == level_length - 1:
#                 result.append(node.val)
                
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
    
#     return result

# # Example usage
# # root = [1,2,3,null,5,null,4]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
# print(right_side_view(root))


# def is_valid_sudoku(board):
#     # Use sets to keep track of seene numbers in rows, cols, and sun-boxes
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
            
#             box_index = (i // 3) * 3 + (j // 3)
            
#             if num in boxes[box_index]:
#                 return False
#             boxes[box_index].add(num)
    
#     return True
    

# Example usage:
# board = [
#     [".",".","4",".",".",".","6","3","."],
#     [".",".",".",".",".",".",".",".","."],
#     ["5",".",".",".",".",".",".","9","."],
#     [".",".",".","5","6",".",".",".","."],
#     ["4",".","3",".",".",".",".",".","1"],
#     [".",".",".","7",".",".",".",".","."],
#     [".",".",".","5",".",".",".",".","."],
#     [".",".",".",".",".",".",".",".","."],
#     [".",".",".",".",".",".",".",".","."]
# ]
# print(is_valid_sudoku(board))  # Output should be False



def solve_sudoku(board):
    def is_valid(board, r, c, num):
        # Check the row
        for i in range(9):
            if board[r][i] == num:
                return False
        
        # Check the col
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