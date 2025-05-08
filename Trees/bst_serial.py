"""Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible."""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Codec:
    """Helper function to reconstruct BST within given bounds"""
    def _build_tree(self, values, lower, upper):
        if not values or values[0] < lower or values[0] > upper:
            return None
        
        val = values.pop(0)
        root = TreeNode(val)
        
        root.left = self._build_tree(values, lower, val)
        root.right = self._build_tree(values, val, upper)
        
        return root
    
    
    def serialize(self, root):
        def preorder(node):
            if not node:
                return []
            
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        # print(','.join(preorder(root)))
        return ','.join(preorder(root))
    
    
    def deserialize(self, data):
        if not data:
            return None
        
        values = list(map(int, data.split(',')))
        
        return self._build_tree(values, float('-inf'), float('inf'))
    
    
    
    
# Example Tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)  # Example: "2,1,3"

deserialized_root = codec.deserialize(serialized)
print("Deserialized Root Value:", deserialized_root.val)  # Output: 2    