class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
       
    
def is_leaf(node):
    return not node.left and not node.right
    
    
def add_left_boundary(node, result):
    while node:
        if not is_leaf(node):
            result.append(node.val)
            
        if node.left:
            node = node.left
        else:
            node = node.right
    
        
def add_leaves(node, result):
    if not node:
        return
        
    if is_leaf(node):
        result.append(node.val)
        
    add_leaves(node.left, result)
    add_leaves(node.right, result)
        
        
def add_right_boundary(node, result):
    stack = []
        
    while node:
        if not is_leaf(node):
            stack.append(node.val)
                
        if node.right:
            node = node.right                   
        else:
            node = node.left
                    
    while stack:
        result.append(stack.pop())

        
        
def boundary_of_binary_tree(root):
    if not root:
        return []
           
    result = []
    
    # Add the root node if it is not a leaf
    if not is_leaf(root):
        result.append(root.val)
    
    # Add the left boundary excluding leafs
    add_left_boundary(root.left, result)
    
    # Add all leaf nodes
    add_leaves(root, result)
    
    # Add the right boundary excluding leafs, in reverse order
    add_right_boundary(root.right, result)
    
    return result
    
    
# Constructing a binary tree:
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
#      / \
#     8   9

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(9)))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))
print(boundary_of_binary_tree(root))