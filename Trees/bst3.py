class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_BST(root):
    """
    Determines if a binary tree is a valid Binary Search Tree (BST).

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree is a valid BST, False otherwise.
    """
    
    # Use a helper function with min/max bounds for each node
    def validate(node, min_val, max_val):
        if not node:
            return True # This is because an empty tree is a valid BST
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    
    return validate(root, float('-inf'), float('inf'))

# Example Usage:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(is_valid_BST(root))