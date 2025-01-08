class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_second_minimum_value(root):
    if not root:
        return -1
    if not root.left and not root.right:
        return -1

    # Get the values of the left and right children
    left_val = root.left.val
    right_val = root.right.val
    
    # If the left value equals root, we need to look deeper into the left subtree
    if left_val == root.val:
        left_val = find_second_minimum_value(root.left)
        
    # If the right value equals root, we need to look deeper into the left subtree
    if right_val == root.val:
        right_val = find_second_minimum_value(root.right)
        
    if left_val != -1 and right_val != -1:
        return min(left_val, right_val)
    
    return max(left_val, right_val)

# Example Usage
root1 = TreeNode(2)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)
print(find_second_minimum_value(root1))
