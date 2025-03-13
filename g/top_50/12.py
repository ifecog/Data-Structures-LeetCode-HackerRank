class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def getDirections(root, startValue, destValue):
    def findPath(node, target, path):
        if not node:
            return False
        if node.val == target:
            return True
        
        # Check the left subtree
        path.append('L')
        if findPath(node.left, target, path):
            return True
        path.pop()
        
        # Check the right subtree
        path.append('R')
        if findPath(node.right, target, path):
            return True
        path.pop()
        
    # Root to start value
    root_to_start = []
    findPath(root, startValue, root_to_start)
    
    # Root to destination value
    root_to_dest = []
    findPath(root, destValue, root_to_dest)
    
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