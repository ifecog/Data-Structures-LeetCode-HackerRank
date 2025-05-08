from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            
            else:
                result.append('null')
                
        return ','.join(result)
    
    
    def deserialize(self, data):
        if not data:
            return None
        
        values = data.split(',')
        root = TreeNode(int(values[0]))
        
        queue = deque([root])
        i = 1
        
        while queue:
            node = queue.popleft()
            
            if values[i] != 'null':
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
                
            i += 1
            
            if i < len(values) and values[i] != 'null':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            
            i += 1
            
        return root
    
    # Example Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
serialized = codec.serialize(root)
print("Serialized:", serialized)  # Example: "1,2,3,null,null,4,5"

deserialized_root = codec.deserialize(serialized)
print("Deserialized Root Value:", deserialized_root.val)