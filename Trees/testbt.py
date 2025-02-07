from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    root1.val += root2.val
    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)
    
    return root1


def min_depth(root):
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append(node.right, depth + 1)
            
    
    return 1 + min(min_depth(root.left), min_depth(root.right))