class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def binary_tree_paths(root):
    """
    Given the root of a binary tree, return all root-to-leaf paths in any order.

    A leaf is a node with no children.

    Args:
        root (int): The root of the binary tree

    Returns:
        list: A list of the possible tree paths
    """
    
    if not root:
        return []
    
    result = []
    
    def dfs(node, path):
        # Append the curret node's value to the path
        path.append(str(node.val))
        
        if not node.left and not node.right:            
            result.append('->'.join(path))
            
        else:
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        
        # Backtrack to explore other paths
        path.pop()

    dfs(root, [])
    
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print(binary_tree_paths(root))