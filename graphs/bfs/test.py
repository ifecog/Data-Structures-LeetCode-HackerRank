from collections import defaultdict, deque

def alienOrder(words):
    n = len(words)
    
    graph = defaultdict(set)
    in_degree = {char: 0 for word in words for char in word}

    for i in range(n - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))

        if len(w1) > len(w2) and w1[:min_length] == w2:
            return ''

        for j in range(min_length):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1

                break

    queue = deque([char for char in in_degree if in_degree[char] == 0])
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)

        for neighbor in graph[char]:
            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ''.join(order) if len(in_degree) == len(order) else ''

# Example usage 
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienOrder(words))  


def find_order(num_courses, prerequisites):
    pre_to_course = defaultdict(list)
    in_degree = [0] * num_courses

    for course, pre in prerequisites:
        pre_to_course[pre].append(course)
        in_degree[course] += 1

    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for nearest_course in pre_to_course[course]:
            in_degree[nearest_course] -= 1

            if in_degree[nearest_course] == 0:
                queue.append(nearest_course)

    return order if len(order) == num_courses else []

# Example usage
numCourses = 2
prerequisites = [[1, 0]]
print(find_order(numCourses, prerequisites))


def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    fresh_oranges = 0
    
    queue = deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

            elif grid[i][j] == 1:
                fresh_oranges += 1

    minutes_required = 0
    while queue:
        i, j, minutes = queue.popleft()
        minutes_required = max(minutes_required, minutes)

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh_oranges -= 1
                queue.append((ni, nj, minutes + 1))
    
    return minutes_required if fresh_oranges == 0 else -1

# Example usage
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

print(orangesRotting(grid1))


def findAllRecipes(recipes, ingredients, supplies):
    ingredients_to_recipes = defaultdict(list)
    in_degree = {recipe: 0 for recipe in recipes}

    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            ingredients_to_recipes[ingredient].append(recipe)
            in_degree[recipe] += 1

    queue = deque(supplies)
    result = []

    while queue:
        ingredient = queue.popleft()

        for recipe in ingredients_to_recipes[ingredient]:
            in_degree[recipe] -= 1

            if in_degree[recipe] == 0:
                result.append(recipe)
                queue.append(recipe)

    return result
    
# Example usage
recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "cheese"], ["sandwich", "patty"]]
supplies = ["yeast", "flour", "cheese", "patty"]
print("Recipes that can be created:", findAllRecipes(recipes, ingredients, supplies))

def min_knight_moves(N, start, end):
    (x1, y1) = start
    (x2, y2) = end

    directions = [(1, -2), (1, 2), (-1, -2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

    if (x1, y1) == (x2, y2):
        return 0

    queue = deque([(x1, y1, 0)])
    visited = {x1, y1}

    while queue:
        x, y, hops = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (nx, ny) == (x2, y2):
                return hops + 1

            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, hops + 1))

    return -1

# Example usage:
N = 8  # Chessboard size (8x8)
start = (0, 0)  # Starting position of the Knight
end = (7, 7)  # Destination position
print(min_knight_moves(N, start, end))


def shortest_bridge(grid):
    n = len(grid)
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def dfs(i, j, island):
        if not(0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
            return

        grid[i][j] = island

        for di, dj in directions:
            dfs(i + di, j + dj, island)

    island = 2
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j, island)
                island += 1

    queue = deque()
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    while queue:
        i, j, flips = queue.popleft()

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < n:
                if grid[ni][nj] == 3:
                    return flips

                if grid[ni][nj] == 0:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, flips + 1))

    return -1


grid = [
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
]

print(shortest_bridge(grid))

