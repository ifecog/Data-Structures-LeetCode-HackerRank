from collections import deque

# Possible movements for a Knight
coordinates = [
    (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
]

# Function to check of the coordinates are within the boundary
def is_within_board(x, y, N):
    return 0 <= x < N and 0 <= y < N


# Main function to find the minimum knight moves
def min_knight_moves(N, start, end):
    """Given a N x N chessboard, find the shortest hops needed by a Knight to reach from (x1, y1) to (x2, y2) on chessboard

    Args:
        N (int): Size of the chessboard
        start (tuple): Starting position of the knight
        end (tuple): ending position of the knight

    Returns:
        _type_: _description_
    """
    
    # This is solved using the Breadth-First-Search (BFS) approach
    
    (x1, y1) = start
    (x2, y2) = end
    
    if (x1, y1) == (x2, y2):
        return 0
    
    # Queue for BFS, storing (current_position, hop_count)
    queue = deque([(x1, y1, 0)])
    visited_positions = {x1, y1}
    
    while queue:
        x, y, hops = queue.popleft()
        
        # Explore all possible knight moves
        for dx, dy in coordinates:
            nx, ny = x + dx, y + dy
            
            if (nx, ny) == (x2, y2):
                return hops + 1
            
            # If the cell is within the boundary and unvisited, add it to thr visited positions
            if is_within_board(nx, ny, N) and (nx, ny) not in visited_positions:
                queue.append((nx, ny, hops + 1))
                visited_positions.add((nx, ny))
    
    # If the target is unreachable (which theoretically shouldn't happen on a chess board)
    return -1


# Example usage:
N = 8  # Chessboard size (8x8)
start = (0, 0)  # Starting position of the Knight
end = (7, 7)  # Destination position
print(min_knight_moves(N, start, end))