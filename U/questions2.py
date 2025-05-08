"""
1. There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

2. You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

3. You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1."

4. There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

"""
def count_consecutive_pairs(query):
    max_n = max(x[0] for x in query)
    line = [0] * (max_n + 1)
    
    same_color_pairs = 0
    result = []
    
    for idx, color in query:
        left_same = (idx > 0 and line[idx - 1] == line[idx] and line[idx] != 0)
        right_same = (idx < max_n and line[idx + 1] == line[idx] and line[idx] != 0)
        
        if left_same:
            same_color_pairs -= 1
        if right_same:
            same_color_pairs -= 1
            
        line[idx] = color
        
        left_same = (idx > 0 and line[idx - 1] == line[idx])
        right_same = (idx < max_n and line[idx + 1] == line[idx])
        
        if left_same:
            same_color_pairs += 1
        if right_same:
            same_color_pairs += 1
            
        result.append(same_color_pairs)
    
    return result

# Example usage
query = [[2,1],[3,1],[4,3],[5,1],[4,1]]
print(count_consecutive_pairs(query))

def rotateTheBox(box):
    m, n = len(box), len(box[0])
    
    rotated = [['.'] * m for _ in range(n)]
    for r in range(m):
        for c in range(n):
            rotated[c][m - 1 - r] = box[r][c]
            
    for col in range(m):
        bottom = n - 1
        
        for row in range(n - 1, -1, -1):
            if rotated[row][col] == '*':
                bottom = row - 1
                
            if rotated[row][col] == '#':
                rotated[row][col] = '.'
                rotated[bottom][col] = '#'
                bottom -= 1
                
    return rotated

boxGrid = [["#",".","*","."],
            ["#","#","*","."]]

output = rotateTheBox(boxGrid)
for row in output:
    print("".join(row))



def collect_sticks(forest, bird):
    n = len(forest)
    
    pos = bird
    direction = 1
    
    nest_size = 0
    picked_indices = []
    
    while nest_size < 100:
        if not (0 <= pos < n):
            break
        
        while 0 <= pos < n and forest[pos] == 0:
            pos += direction
            
        # Collect the sticks
        nest_size += forest[pos]
        picked_indices.append(pos)
        
        # Mark that position as visited
        forest[pos] = 0
        
        direction *= -1
    
    return picked_indices
    

forest=[10,50,0,100] 
bird=2
print(collect_sticks(forest, bird))

def maxRating(diff):
    curr_rating = 1500
    max_rating = 1500
    
    for change in diff:
        curr_rating += change
        max_rating = max(max_rating, curr_rating)
        
    return [max_rating, curr_rating]
    
diff=[10,50,-10,100]
print(maxRating(diff))