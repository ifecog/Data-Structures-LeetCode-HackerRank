from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Codec:
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
