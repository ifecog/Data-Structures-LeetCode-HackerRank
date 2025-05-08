from collections import Counter, defaultdict, deque
import bisect, random, heapq


def find_robots_with_matching_query(grid, query):
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    
    def bfs(i, j, direction):
        visited = set()
        queue = deque([(i, j, 0)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            nx, ny = x + direction[0], y + direction[1]
            
            if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] == 'X':
                return distance + 1
            
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, distance + 1))
                
        return -1
    
    robots = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 'O']
    result = []
    
    for r, c in robots:
        distances = [bfs(r, c, dir) for dir in directions]
        
        if distances == query:
            result.append([r, c])
            
    return result

# Example usage
grid = [
    
    ['O', 'E', 'E', 'E', 'X'],
    ['E', 'O', 'X', 'X', 'X'],
    ['E', 'E', 'E', 'E', 'E'],
    ['X', 'E', 'O', 'E', 'E'],
    ['X', 'E', 'X', 'E', 'X']
]
query = [2, 2, 4, 1]

print(find_robots_with_matching_query(grid, query))