from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def subtree_with_all_deepest(root):
    def dfs(node):
        if not node:
            return (0, None)
        
        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca = dfs(node.right)
        
        if left_depth > right_depth:
            return (left_depth + 1, left_lca)
        
        elif right_depth > left_depth:
            return (right_depth + 1, right_lca)
        
        # If both are equal, this node is the lca
        else:
            return (left_depth + 1, node)
        
    return dfs(root)[1]
        
# def subtree_with_all_deepest(root):
#     def find_deepest_nodes(root):
#         if not root:
#             return []
        
#         queue = deque([root])
        
#         # Outer initialization to store deepest nodes from any level
#         deepest_nodes = []
        
#         while queue:
#             level_size = len(queue)
            
#             # Inner initialization to clear the list on each level
#             deepest_nodes = []
            
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 deepest_nodes.append(node)
                
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
        
#         return deepest_nodes
    
#     def find_lca(root, nodes):
#         if not root:
#             return None
#         if root in nodes:
#             return root
        
#         left = find_lca(root.left, nodes)
#         right = find_lca(root.right, nodes)
#         if left and right:
#             return root
        
#         return left if left else right
    
#     deepest_nodes = find_deepest_nodes(root)
#     if not deepest_nodes:
#         return None
    
#     return find_lca(root, set(deepest_nodes))


# Example usage:
# Constructing a binary tree:
#        3
#       / \
#      5   1
#     / \ / \
#    6  2 0  8
#      / \
#     7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Find the smallest subtree with all the deepest 
subtree_root = subtree_with_all_deepest(root)
print(subtree_root.val)
    