class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def kth_smallest(root, k):
    # Initialze an empty stack to store nodes for traversals
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
        
# # Example usage:
# # Construct a binary search tree: [3,1,4,null,2]
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)

# k = 2
# print(kth_smallest(root, k))

def right_side_view(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.pop(0)
            
            if i == level_length - 1:
                result.append(node.val)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Example usage
# root = [1,2,3,null,5,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(right_side_view(root))