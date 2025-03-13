from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def min_depth(root):
    if not root:
        return 0
    
    # if not root.left or not root.right:
    #     return 1 + max(min_depth(root.left), min_depth(root.right))
    
    # return 1 + min(min_depth(root.left), min_depth(root.right))

    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    

# def min_depth(root):
#     if not root:
#         return 0
    
#     # queue = deque([(root, 1)])
#     # while queue:
#     #     node, depth = queue.popleft()
        
#     #     if not node.left and not node.right:
#     #         return depth
        
#     #     if node.left:
#     #         queue.append((node.left, depth + 1))
#     #     if node.right:
#     #         queue.append((node.right, depth + 1))
    
#     return 1 + min(min_depth(root.left), min_depth(root.right))
            
            
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(min_depth(root))