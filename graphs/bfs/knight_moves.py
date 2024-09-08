from collections import deque

# Possible movements for a Knight
knight_moves = [
    (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
]

def is_within_board(x, y, N):
    return 0 <= x < N and 0 <= y < N


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
    
    x1, y1 = start
    x2, y2 = end
    
    if (x1, y1) == (x2, y2):
        return 0
    
    # Queue for BFS, storing (current_position, hop_count)
    queue = deque([(x1, y1, 0)])
    visited_positions = set([x1, y1])
    
    while queue:
        x, y, hops = queue.popleft()
        
        # Explore all possible knight moves
        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            
            if (new_x, new_y) == (x2, y2):
                return hops + 1
            
            if is_within_board(new_x, new_y, N) and (new_x, new_y) not in visited_positions:
                queue.append((new_x, new_y, hops + 1))
                visited_positions.add((new_x, new_y))
    
    # If the target is unreachable (which theoretically shouldn't happen on a chess board)
    return -1


# Example usage:
N = 8  # Chessboard size (8x8)
start = (0, 0)  # Starting position of the Knight
end = (7, 7)  # Destination position
print(min_knight_moves(N, start, end))