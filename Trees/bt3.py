class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# def in_order_traversal(root):
#     result = []
    
#     def in_order(node):
#         if not node:
#             return 
        
#         in_order(node.left)
#         result.append(node.val)
#         in_order(node.right)
    
#     in_order(root)
    
#     return result


def pre_order_traversal(root):
    result = []
    
    def pre_order(node):
        if not node:
            return
        
        result.append(node.val)
        pre_order(node.left)
        pre_order(node.right)
    
    pre_order(root)
    
    return result
    

# Example usage
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# print(in_order_traversal(root))
print(pre_order_traversal(root))