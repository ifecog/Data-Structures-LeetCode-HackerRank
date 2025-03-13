# def justify_line(line, line_length, maxWidth):
#     if len(line) == 1:
#         # If there is only one word, left justify it
#         return line[0] + ' ' * (maxWidth - line_length)
    
#     # Calculate total spaces and gaps
#     total_spaces = maxWidth - line_length
#     gaps = len(line) - 1
#     spaces_per_gap = total_spaces // gaps
#     extra_spaces = total_spaces % gaps
    
#     justified_line = []
#     for i in range(len(line) - 1):
#         justified_line.append(line[i])
#         justified_line.append(' ' * (spaces_per_gap + (1 if i < extra_spaces else 0)))
        
#     justified_line.append(line[-1])
#     return ''.join(justified_line)


# def left_justify(line, maxWidth):
#     return ' '.join(line) + ' ' * (maxWidth - len(' '.join(line)))



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def preorder(root):
    result = []
    def do(node):
        if not node:
            return
        result.append(node.val)
        do(node.left)
        do(node.right)
        
    do(root)
    
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(preorder(root))
