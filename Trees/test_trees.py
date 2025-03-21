class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def constructFromPrePost(preorder, postorder):
    if not preorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    if len(preorder) == 1:
        return root
    
    left_root_val = preorder[1]
    left_root_idx = postorder.index(left_root_val)
    
    left_postorder = postorder[:left_root_idx + 1]
    right_postorder = postorder[left_root_idx + 1:-1]
    
    left_preorder = preorder[1:len(left_postorder) + 1]
    right_preorder = preorder[len(left_postorder) + 1:]
    
    root.left = constructFromPrePost(left_preorder, left_postorder)
    root.right = constructFromPrePost(right_preorder, right_postorder)
    
    return root

def print_tree(root):
    if not root:
        return []
    return [root.val] + print_tree(root.left) + print_tree(root.right)

pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
tree = constructFromPrePost(pre, post)

print(print_tree(tree))