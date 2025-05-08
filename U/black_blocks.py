"""You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.

You are also given a 0-indexed 2D integer matrix coordinates, where coordinates[i] = [x, y] indicates that the cell with coordinates [x, y] is colored black. All cells in the grid that do not appear in coordinates are white.

A block is defined as a 2 x 2 submatrix of the grid. More formally, a block with cell [x, y] as its top-left corner where 0 <= x < m - 1 and 0 <= y < n - 1 contains the coordinates [x, y], [x + 1, y], [x, y + 1], and [x + 1, y + 1].

Return a 0-indexed integer array arr of size 5 such that arr[i] is the number of blocks that contains exactly i black cells."""

from collections import defaultdict

def countBlackBlocks(m, n, coordinates):
    # Dictionary to count how many black cells are in each 2x2 block, keyed by top-left (x, y)
    block_counts = defaultdict(int)
    
    for i, j in coordinates:
        for di in (0, -1):
            for dj in (0, -1):
                ni, nj = i + di, j + dj
                
                if 0 <= ni < m - 1 and 0 <= nj < n - 1:
                    block_counts[(ni, nj)] += 1
                    
    result = [0] * 5
    for count in block_counts.values():
        result[count] += 1
       
    total_blocks = (m - 1) * (n - 1)
    result[0] = total_blocks - sum(result[1:])
    
    return result

# Example usage
m = 3
n = 3
coordinates = [[0,0],[1,1]]

print(countBlackBlocks(m, n, coordinates))