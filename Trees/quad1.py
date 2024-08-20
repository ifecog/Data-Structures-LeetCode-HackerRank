class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        
    
def construct(grid):
    # Helper function to check if all the values in the sub-grid are uniform
    def is_uniform(x, y, length):
        val = grid[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if grid[i][j] != val:
                    return False, None
        
        return True, val
    
    
    # Recursive function to construct the Quad-Tree
    def construct_recursive(x, y, length):
        uniform, val = is_uniform(x, y, length)
        if uniform:
            return Node(val=bool(val), isLeaf=True)
        
        half = length // 2
        topLeft = construct_recursive(x, y, half)
        topRight = construct_recursive(x, y + half, half)
        bottomLeft = construct_recursive(x + half, y, half)
        bottomRight = construct_recursive(x + half, y + half, half)
        
        return Node(val=True, isLeaf=False, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
    
    return construct_recursive(0, 0, len(grid))

# Example usage:
grid = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

quad_tree_root = construct(grid)

print(quad_tree_root.val)