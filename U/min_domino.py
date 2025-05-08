"""In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1."""


def min_domino_rotations(tops, bottoms):
    def check(target):
        top_rotations = bottom_rotations = 0
        
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            
            elif tops[i] != target:
                top_rotations += 1
                
            elif bottoms[i] != target:
                bottom_rotations += 1
                
        return min(top_rotations, bottom_rotations)
    
    rotations = min(check(tops[0]), check(bottoms[0]))
    
    return rotations if rotations != float('inf') else -1

# Example Usage:
tops = [2, 1, 2, 4, 2, 2]
bottoms = [5, 2, 6, 2, 3, 2]
print(min_domino_rotations(tops, bottoms))  # Output: 2



   