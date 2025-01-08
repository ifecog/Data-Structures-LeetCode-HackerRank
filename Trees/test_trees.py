class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Second minumum value in a BT
def find_second_minimum_value(root):
    if not root:
        return -1
    if not root.left and not root.right:
        return -1
    
    left_val = root.left.val
    right_val = root.right.val
    
    if left_val == root.val:
        left_val = find_second_minimum_value(root.left)
    if right_val == root.val:
        right_val = find_second_minimum_value(root.right)
        
    if left_val != -1.0 and right_val != -1.0:
        return min(left_val, right_val)
    
    return max(left_val, right_val)

# Example Usage
root1 = TreeNode(2)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)
print(find_second_minimum_value(root1))



# # Find mode in a BST
# def find_mode(root):
#     if not root:
#         return []
    
#     prev = None
#     count = 0
#     max_count = 0
#     modes = 0
    
#     def in_order(node):
#         nonlocal prev, count, max_count, modes
        
#         if not node:
#             return
        
#         # Left subtree
#         in_order(node.left)
        
#         # Process the current node
#         if node.val == prev:
#             count += 1
#         else:
#             count = 1
#         prev = node.val
        
#         # Update modes list
#         if count > max_count:
#             max_count = count
#             modes = [node.val]
#         elif count == max_count:
#             modes.append(node.val)
        
#         # Right subtree
#         in_order(node.right)
        
#     in_order(root)
    
#     return modes

# # Example Usage:
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(2)

# print(find_mode(root))


# # Min distance between BST nodes
# def min_diff_in_BST(root):
#     min_diff = float('inf')
#     prev = None
    
#     stack = []
#     while stack or root:
#         while root:
#             stack.append(root)
#             root = root.left
        
#         root = stack.pop()
#         if prev is not None:
#             min_diff = min(min_diff, root.val - prev)
        
#         prev = root.val
#         root = root.right
    
#     return min_diff
    

# # Example usage
# root1 = TreeNode(4)
# root1.left = TreeNode(2)
# root1.right = TreeNode(6)
# root1.left.left = TreeNode(1)
# root1.left.right = TreeNode(3)
# print(min_diff_in_BST(root1))



# # Validity of BST
# def is_valid_BST(root):
#     def validate(node, min_val, max_val):
#         if not node:
#             return True
        
#         if node.val <= min_val or node.val >= max_val:
#             return False
        
#         return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
    
#     return validate(root, float('-inf'), float('inf'))

# # Example Usage:
# root = TreeNode(2)
# root.left = TreeNode(1)
# root.right = TreeNode(3)

# print(is_valid_BST(root))


# # Right Side View of a Binary Tree
# from collections import deque

# def right_side_view(root):
#     result = []
#     if not root:
#         return result
    
#     queue = deque([root])
#     while queue:
#         level_size = len(queue)
        
#         for i in range(level_size):
#             node = queue.popleft()
            
#             if i == level_size - 1:
#                 result.append(node.val)
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)

#     return result

# # Example usage
# # root = [1,2,3,null,5,null,4]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)
# print(right_side_view(root))


# # Level Order Traversal
# from collections import deque

# def level_order_traversal(root):
#     if not root:
#         return
    
#     queue = deque([root])
#     while queue:
#         level_size = len(queue)
#         level = []
#         for _ in range(level_size):
#             node = queue.popleft()
#             level.append(node.val)
            
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
        
#         print(' '.join(map(str, level)))
    
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)

# level_order_traversal(root)


# # Lowest Common Ancestor
# def lowest_common_ancestor(root, p, q):
#     if not root:
#         return
     
#     if p.val < root.val and q.val < root.val:
#         return lowest_common_ancestor(root.left, p, q)
     
#     if p.val > root.val and q.val > root.val:
#         return lowest_common_ancestor(root.right, p, q)        
     
#     return root
 
#  # Example usage:
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

       
# # Kth Smallest Element
# def kth_smallest(root, k):
#     stack = []
    
#     while stack or root:
#         while root:
#             stack.append(root)
#             root = root.left
        
#         root = stack.pop()
#         k -= 1
#         if k == 0:
#             return root.val
        
#         root = root.right
    
#     return stack

# # Example usage:
# # Construct a binary search tree: [3,1,4,null,2]
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.right = TreeNode(2)

# k = 2
# print(kth_smallest(root, k))
