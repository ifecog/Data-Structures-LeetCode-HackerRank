from collections import deque


def min_knight_moves(N, start, end):
    directions = [
        (1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]
    
    (x1, y1), (x2, y2) = start, end
    
    if (x1, y1) == (x2, y2):
        return 0
    
    visited_positions = {x1, y1}
    queue = deque([(x1, y1, 0)])
    
    while queue:
        x, y, hops = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (nx, ny) == (x2, y2):
                return hops + 1
            
            if (0 <= nx < N and 0 <= ny < N) and (nx, ny) not in visited_positions:
                visited_positions.add((ny, ny))
                queue.append((nx, ny, hops + 1))
                
    return -1

# Example usage:
N = 8  # Chessboard size (8x8)
start = (0, 0)  # Starting position of the Knight
end = (7, 7)  # Destination position
print(min_knight_moves(N, start, end))