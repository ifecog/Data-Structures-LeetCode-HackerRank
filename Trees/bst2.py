class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    """Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Args:
        root (int): root of the binary search tree
        p (int): node 1
        q (int): node 2

    Returns:
        _type_: _description_
    """
    
    # If both nodes have values lesser than the root node, move the root node to the left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both nodes have values greater than the root node, move the root node to the right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    return root
    

# Example usage:
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

p = root.left.right.left
q = root.left.right.right

result = lowest_common_ancestor(root, p, q)
print(result.val)  # Output: 4