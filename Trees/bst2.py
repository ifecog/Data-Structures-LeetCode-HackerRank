class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
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