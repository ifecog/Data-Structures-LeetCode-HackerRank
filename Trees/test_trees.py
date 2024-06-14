class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
# 1. Right Side View of a Binary Tree
def right_side_view(root):
    result = []
    if not root:
        return []
    
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
    

# # Example usage
# # root = [1,2,3,null,5,null,4]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
# print(right_side_view(root))


# 2. Lowest Common Ancestor
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    # If both node values have values lesser than the root node, move the root node to the left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both node values have values greater than the root node, move the root node to the right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    return root


# # Example usage:
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)

# p = root.left.right.left
# q = root.left.right.right

# result = lowest_common_ancestor(root, p, q)
# print(result.val)  # Output: 4


# 3. Kth smallest vallue in a binary search tree
def kth_smallest(root, k):
    # Initialize an empty stack to store node for traversal
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
    
    return stack

# Example usage:
# Construct a binary search tree: [3,1,4,null,2]
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 2
print(kth_smallest(root, k))
