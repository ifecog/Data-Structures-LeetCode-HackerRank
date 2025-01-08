from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
def right_side_view(root):
    """Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

    Args:
        root (root): root of the binary tre

    Returns:
        list: _description_
    """
    
    if not root:
        return []
    
    result = []
    
    # queue = [root]
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            # node = queue.pop(0)
            
            # If this is the last node in the current level, add it to the result
            if i == level_length - 1:
                result.append(node.val)
            
            # Add the left and right children to the queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return result

    
# Example usage
# root = [1,2,3,null,5,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(right_side_view(root))
