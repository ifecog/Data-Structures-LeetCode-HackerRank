from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def print_tree(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()
    
          
def invert_tree(root):
    """
    Given the root of a binary tree, invert the tree, and return its root.

    Args:
        root (int): The root of the binary tree

    Returns:
        int: The inverted tree
    """
    
    if not root:
        return None
    
    # root.left, root.right = root.right, root.left
    # invert_tree(root.left)
    # invert_tree(root.right)
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# Constructing the example tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree
inverted_root = invert_tree(root)

# Print the inverted tree
print_tree(inverted_root)