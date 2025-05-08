from collections import deque

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


def reverse_odd_levels(root):
    """
    Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

    For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
    
    Return the root of the reversed tree.

    A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

    The level of a node is the number of edges along the path between it and the root node.

    Args:
        root (int): The root of the binary tree

    Returns:
        int: the binary tree with reversed odd levels
    """
    
    if not root:
        return []
    
    queue = deque([root])
    level = 0
    
    while queue:
        level_size = len(queue)
        level_nodes = list(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        if level % 2 == 1:
            left, right = 0, len(level_nodes) - 1
            
            while left < right:
                level_nodes[left].val, level_nodes[right].val = level_nodes[right].val, level_nodes[left].val
                
                left += 1
                right -= 1
        
        level += 1
        
    return root
    
    
    
    # if not root:
    #     return []
    
    # queue = deque([root])
    # level = 0
    
    # while queue:
    #     level_size = len(queue)
    #     current_level_nodes = []
        
    #     for _ in range(level_size):
    #         node = queue.popleft()
    #         current_level_nodes.append(node)
            
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
                
    
    #     if level % 2 == 1:
    #         values = [node.val for node in current_level_nodes]
    #         reversed_values = values[::-1]
            
    #         # Assign reversed values back to the nodes
    #         for i, node in enumerate(current_level_nodes):
    #             node.val = reversed_values[i]
        
    #     level += 1
        
    # return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

reverse_odd_levels(root)

print_tree(root)