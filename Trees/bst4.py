class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_BST(root):
    """
    Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

    Args:
        root (int): the root value of the BST
    """
    
    min_diff = float('inf')
    prev = None
    
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        if prev is not None:
            min_diff = min(min_diff, root.val - prev)
        
        prev = root.val
        root = root.right
    
    return min_diff
    
    
# Example usage
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
print(min_diff_in_BST(root1))
    
    
    # in_order_values = []
    
    # def in_order(node):
    #     if not node:
    #         return
    #     in_order(node.left)
    #     in_order_values.append(node.val)
    #     in_order(node.right)
    
    # in_order(root)
    
    # min_diff = float('inf')
    # for i in range(len(in_order_values) - 1):
    #     min_diff = min(min_diff, in_order_values[i + 1] - in_order_values[i])
        
    # return min_diff