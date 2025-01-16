class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(root1, root2):
    """
    You are given two binary trees root1 and root2.

    Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

    Return the merged tree.

    Note: The merging process must start from the root nodes of both trees.

    Args:
        root1 (int): The root of the 1st binary tree
        root2 (int): The root of the 2nd binary tree
    """
    
    if not root1:
        return root2
    if not root2:
        return root1
    
    root1.val += root2.val
    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)
    
    return root1

root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

print(merge_trees(root1, root2))