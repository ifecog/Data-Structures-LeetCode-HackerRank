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
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()
    
    
def is_subtree(root, subroot):
    """
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

    Args:
        root (int): The main tree
        subroot (int): The subtree

    Returns:
        bool: True if it is a subtree
    """
    
    if not subroot:
        return True
    if not root:
        return False
    
    def is_identical(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        
        return (
            tree1.val == tree2.val and
            is_identical(tree1.left, tree2.left) and
            is_identical(tree1.right, tree2.right)
        )
    
    if is_identical(root, subroot):
        return True
    
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

# Constructing the subtree:
#    4
#   / \
#  1   2
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

# Check if subRoot is a subtree of root
print(is_subtree(root, subRoot))

