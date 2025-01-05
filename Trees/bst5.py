class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_mode(root):
    """
    Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

    If the tree has more than one mode, return them in any order.

    Args:
        root (int): The root of the BST
    """
    
    if not root:
        return []
    
    prev = None
    count = 0 # Current count of any value
    max_count = 0 # Maximum frequency of any value
    modes = [] # List to store the mode(s)
    
    def in_order(node):
        nonlocal prev, count, max_count, modes
        
        if not node:
            return
        
        # Left subtree
        in_order(node.left)
        
        # Processing the current node
        if node.val == prev:
            count += 1
        else:
            count = 1
        prev = node.val
        
        # Update mode(s) list
        if count > max_count:
            max_count = count
            modes = [node.val]
        elif count == max_count:
            modes.append(node.val)
        
        # Right subtree
        in_order(node.right)
        
    in_order(root)
    
    return modes

# Example Usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)

print(find_mode(root))