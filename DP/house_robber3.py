class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def rob(root):
    """The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

    Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

    Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

    Args:
        root (int): The root of the binary tree representing the firt house

    Returns:
        int: Maximum amount of money the thief can rob without alerting the police
    """
    
    # Memoization dictionary to store computed values
    dp = {}
    
    # Recurssive helper function
    def helper(node):
        if not node:
            return 0
        if node in dp:
            return dp[node]
        
        # Option 1: Rob this node then skip the children and rob the grandchildren
        rob_this = node.val
        if node.left:
            rob_this += helper(node.left.left) + helper(node.left.right)
        if node.right:
            rob_this += helper(node.right.left) + helper(node.right.right)
            
        # Option 2: Do not rob this node, just rob its children
        not_rob_this = helper(node.left) + helper(node.right)
        
        # Take the maximum of the 2 approaches
        dp[node] = max(rob_this, not_rob_this)
        
        return dp[node]
    
    return helper(root)


# Tree construction for the test
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

print(rob(root))