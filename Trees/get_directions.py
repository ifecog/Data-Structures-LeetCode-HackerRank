class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""Step-By-Step Directions From a Binary Tree Node to Another
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t."""
        
def getDirections(root, startValue, destValue):
    def find_path(node, target, path):
        if not node:
            return False        
        if node.val == target:
            return True
        
        path.append('L')
        if find_path(node.left, target, path):
            return True
        path.pop()
        
        path.append('R')
        if find_path(node.right, target, path):
            return True
        path.pop()
        
    root_to_start = []
    find_path(root, startValue, root_to_start)
    
    root_to_dest = []
    find_path(root, destValue, root_to_dest)
    
    lca = 0
    while lca < len(root_to_start) and lca < len(root_to_dest) and root_to_start[lca] == root_to_dest[lca]:
        lca += 1
        
    start_to_lca = ['U'] * (len(root_to_start) - lca)
    lca_to_dest = root_to_dest[lca:]
    
    return ''.join(start_to_lca) + ''.join(lca_to_dest)


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

# Find the path from node 3 to node 6
startValue = 3
destValue = 6
print(getDirections(root, startValue, destValue))