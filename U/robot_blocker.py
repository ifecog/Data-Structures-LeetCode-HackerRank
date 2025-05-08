"""
| O | E | E | E | X |
| E | O | X | X | X |
| E | E | E | E | E |
| X | E | O | E | E |
| X | E | X | E | X |

O = Robot, E = Empty, X = blocker

{{'O','E','E','E','X'},{'E','O','X','X','X'},{'E','E','E','E','E'},{'X','E','O','E','E'},{'X','E','X','E','X'}}

Second input is the query. It’s a 1D array consisting of distance to the closest blocker in the order from left, top, bottom and right.

[2, 2, 4, 1] -> This means distance of 2 to the left blocker, 2 to the top blocker, 4 to the bottom blocker and 1 to the right blocker

The location map boundary is also considered blocker, meaning if the robot hits the boundary it also means it’s hitting the blocker.

Task: Write a function that takes these two inputs and returns the index of the robots (if any) that matches the query that we’re looking for.
Answer: [[1, 1]]    
"""

from collections import deque

def find_robots_with_matching_query(grid, query):
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (1, 0), (0, 1)]
       
    # BFS function to get the distance to the blockers 
    def bfs(i, j, direction):
        visited = set()
        queue = deque([(i, j, 0)])
        
        while queue:
            x, y, distance = queue.popleft()
            
            # Move in the specific direction
            nx, ny = x + direction[0], y + direction[1]
            
            if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny] == 'X':
                return distance + 1

            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, distance + 1))
                
        return -1

    # Find all robots
    robots = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 'O']
    result = []
    
    for r, c in robots:
        distances = [bfs(r, c, dir) for dir in directions]
        
        print(f'Checking robot at ({r}, {c}) -> distances = {distances}')
        
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