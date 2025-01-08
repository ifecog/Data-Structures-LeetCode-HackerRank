# Example Usage
root1 = TreeNode(2)
root1.left = TreeNode(2)
root1.right = TreeNode(5)
root1.right.left = TreeNode(5)
root1.right.right = TreeNode(7)
print(find_second_minimum_value(root1))
