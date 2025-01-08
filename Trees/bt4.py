class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
"""
# def count_nodes(root):
#     if not root:
#         return 0
    
#     return 1 + count_nodes(root.left) + count_nodes(root.right)

from collections import deque

def count_nodes(root):
    if not root:
        return 0
    
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        count += 1
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return count


# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(count_nodes(root))