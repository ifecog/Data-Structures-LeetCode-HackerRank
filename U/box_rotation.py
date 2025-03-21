def rotateTheBox(boxGrid):
    """
    You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

    A stone '#'
    A stationary obstacle '*'
    Empty '.'

    The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

    It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

    Return an n x m matrix representing the box after the rotation described above.

    Args:
        boxGrid (array): An array of elements
    """
    
    
    
    m, n = len(boxGrid), len(boxGrid[0])
    
    # Rotate the box 90degrees clockwise
    rotated = [['.'] * m for _ in range(n)]
    
    for r in range(m):
        for c in range(n):
            rotated[c][m - 1 - r] = boxGrid[r][c]
            
    print(rotated)
            
    # Apply gravity (Make stones fall)
    for col in range(m):
        bottom = n - 1
        
        for row in range(n - 1, -1, -1):
            if rotated[row][col] == '*':
                bottom = row - 1
                
            elif rotated[row][col] == '#':
                rotated[row][col] = '.'
                rotated[bottom][col] = '#'
                
                bottom -= 1
                
    return rotated

boxGrid = [["#",".","*","."],
            ["#","#","*","."]]

output = rotateTheBox(boxGrid)
for row in output:
    print("".join(row))
