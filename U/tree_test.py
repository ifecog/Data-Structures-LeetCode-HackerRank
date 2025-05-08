from collections import deque, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def print_tree(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()
        
def merge_trees_rercursion(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    root1.val += root2.val
    root1.left = merge_trees_rercursion(root1.left, root2.left)
    root1.right = merge_trees_rercursion(root1.right, root2.right)
    
    return root1


def merge_trees(root1, root2):
    if not root1:
        return root2
    if not root2:
        return root1
    
    stack = deque([(root1, root2)])
    while stack:
        node1, node2 = stack.popleft()
        
        if not node1 or not node2:
            continue
        
        node1.val += node2.val
        
        if node1.left and node2.left:
            stack.append((node1.left, node2.left))
        elif not node1.left:
            node1.left = node2.left
        
        if node1.right and node2.right:
            stack.append((node1.right, node2.right))
        elif not node1.right:
            node1.right = node2.right
            
    return root1


# Create first tree
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
root1.left.left = TreeNode(5)

# Create second tree
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(7)

print("Tree 1:")
print_tree(root1)

print("Tree 2:")
print_tree(root2)

# Merge trees (recursive)
merged_recursive = merge_trees(root1, root2)
print("Merged Tree (Recursive):")
print_tree(merged_recursive)
