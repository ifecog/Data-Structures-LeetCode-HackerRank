# 1. Bus Routes
from collections import defaultdict, deque

def num_buses_to_destination(routes, source, target):
    if source == target:
        return 0
    
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)
            
    visited_stops = set([source])
    queue = deque([(source, 0)])
    
    while queue:
        current_stop, buses_taken = queue.popleft()
        
        if current_stop == target:
            return buses_taken
        
        current_to_routes_copy = stop_to_routes[current_stop].copy()
        for route_index in current_to_routes_copy:
            for next_stop in routes[route_index]:
                if next_stop not in visited_stops:
                    queue.append((next_stop, buses_taken + 1))
                    visited_stops.add(next_stop)
            
        stop_to_routes[current_stop].remove(route_index)
        
    
    return -1

# Example usage:
routes1 = [[1,2,7],[3,6,7]]
source1 = 1
target1 = 6
print(num_buses_to_destination(routes1, source1, target1))  # Output: 2

routes2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source2 = 15
target2 = 12
print(num_buses_to_destination(routes2, source2, target2))  # Output: -1


# 2. Find the Closest Palindrome

def nearest_palindrome(n):
    n = int(n)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    
    def get_smaller_palindrome(x):
        x -= 1
        while x > 0 and not is_palindrome(str(x)):
            x -= 1
        
        return x
    
    
    def get_greater_palindrome(x):
        x += 1
        while True:
            if is_palindrome(str(x)):
                return x
            x += 1
            
    smaller_palindrome = get_smaller_palindrome(n)
    greater_palindrome = get_greater_palindrome(n)
    
    result = str(smaller_palindrome) if abs(n - smaller_palindrome) <= abs(greater_palindrome - n) else str(greater_palindrome)
    
    return result


# Example usage:
n = "1234"
output = nearest_palindrome(n)
print(output)


# 3. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
def longest_subarray(nums, limit):
    min_queue = deque()
    max_queue = deque()
    
    left = 0
    result = 0
    
    for right, num in enumerate(nums):
        while max_queue and num > max_queue[-1]:
            max_queue.pop()
        max_queue.append(num)
        
        while min_queue and num < min_queue[-1]:
            min_queue.pop()
        min_queue.append(num)
        
        while max_queue[0] - min_queue[0] > limit:
            if max_queue[0] == nums[left]:
                max_queue.popleft()
            
            if min_queue[0] == nums[left]:
                min_queue.popleft()
            
            left += 1
            
        result = max(result, right - left + 1)
        
    return result

# Example usage:
nums = [8, 2, 4, 7]
limit = 4
output = longest_subarray(nums, limit)
print(output)


# 4. Merge Intervals
def merge(intervals):
    intervals.sort(key=lambda i: i[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merge(intervals)
print(result)


# 5. Number of Islands
def num_islands(grid):
    islands_count = 0
    
    def dfs(row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                islands_count += 1
                
                dfs(i, j)
    
    return islands_count

# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid))


# 6. Longest Repeating Character Replacement
def character_replacement(s, k)