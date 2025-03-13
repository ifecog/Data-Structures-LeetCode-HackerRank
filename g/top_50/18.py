from collections import deque

def racecar(target):
    queue = deque([(0, 1, 0)])
    visited = set((0, 1))
    
    while queue:
        pos, speed, moves = queue.popleft()
        
        if pos == target:
            return moves
        
        # Move A (Acceleration)
        new_pos = pos + speed
        new_speed = speed * 2
        if (new_pos, new_speed) not in visited and 0 <= new_pos <= 2 * target:
            visited.add((new_pos, new_speed))
            queue.append((new_pos, new_speed, moves + 1))
            
        # Move R (Reverse)
        new_speed = -1 if speed > 0 else 1
        if (pos, new_speed) not in visited:
            visited.add((pos, new_speed))
            queue.append((pos, new_speed, moves + 1))
            
    return -1


# Example usage
target = 3
print(racecar(target))