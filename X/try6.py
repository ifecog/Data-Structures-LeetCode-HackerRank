class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def kth_smallest(root, k):
    # Initialize an empty stack to store nodes for traversal
    stack = []
    
    while stack or root:
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

k = 1
print(kth_smallest(root, k))