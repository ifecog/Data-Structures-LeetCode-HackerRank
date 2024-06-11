class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def kth_smallest(root, k):
    """Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

    Args:
        root (int): root of the BST
        k (int): parameter

    Returns:
        int: kth smallest value
    """
    
    # Method 2
    stack = []
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        
        root = root.right
    
    return -1
        
# Example usage:
# Construct a binary search tree: [3,1,4,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 2
print(kth_smallest(root, k))


    # Method 1
    # # Initialize an empty stack and counter to keep track of the number of visited nodes
    # stack = []
    # count = 0
    # current = root
    
    # while stack or current:
    #     # Start from the root node and push all left child nodes to the stack until the leftmost node (smallest) is reached.
    #     while current:
    #         stack.append(current)
    #         current = current.left
        
    #     # Pop nodes one by one incrementing the counter for every op action.
    #     current = stack.pop()
    #     count += 1
        
    #     # If counter becomes equal to k, return the value of the current node.
    #     if count == k:
    #         return current.val
        
    #     current = current.right
    
    # return -1
    