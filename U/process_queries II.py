"""There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

    For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
    For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.

Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise."""

import bisect

def can_place_blocks(queries):
    obstacles = []
    result = []
    
    for q in queries:
        if q[0] == 1:
            bisect.insort(obstacles, q[1])
        
        elif q[0] == 2:
            x, sz = q[1], q[2]
            can_place = False
            
            # Get all obstacles <= x
            idx = bisect.bisect_right(obstacles, x)
            
            # Check the first gap from 0 to first obstacle
            if idx == 0:
                if x >= sz:
                    can_place = True
                    
            else:
                # Before first obstacle
                if obstacles[0] >= sz:
                    can_place = True
                    
                # Between obstacles
                for i in range(1, idx):
                    if obstacles[i] - obstacles[i - 1] >= sz:
                        can_place = True
                        break
                    
                # After last obstacle up to x
                if not can_place and x - obstacles[idx - 1] >= sz:
                    can_place = True
                    
            result.append(can_place)
            
    return result

queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
print(can_place_blocks(queries))

# def can_place_blocks(queries):
#     # Initialize with 0 as a virtual obstaclee at the start
#     obstacles = [0]
#     result = []
    
#     for q in queries:
#         if q[0] == 1:
#             x = q[1]
#             bisect.insort(obstacles, x)
            
#         elif q[0] == 2:
#             x, sz = q[1], q[2]
#             can_place = False
            
#             # Get all obstacles <= x
#             idx = bisect.bisect_right(obstacles, x)
            
#             for i in range(1, idx):
#                 if obstacles[i] - obstacles[i - 1] >= sz:
#                     can_place = True
#                     break
                
#             if not can_place:
#                 last_obstacle = obstacles[idx - 1] if idx > 0 else 0
                
#                 if x - last_obstacle >= sz:
#                     can_place = True
                    
#             result.append(can_place)
    
#     return result

# queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
# print(can_place_blocks(queries))


# from sortedcontainers import SortedList

# def can_place_blocks(queries):
#     obstacles = SortedList([0])
#     result = []
    
#     for q in queries:
#         if q[0] == 1:
#             obstacles.add(q[1])
#         else:
#             x, sz = q[1], q[2]
#             idx = obstacles.bisect_right(x)
#             can_place = False

#             # Check between obstacle[i-1] and obstacle[i]
#             for i in range(1, idx):
#                 if obstacles[i] - obstacles[i - 1] >= sz:
#                     can_place = True
#                     break
            
#             # Check after the last obstacle till x
#             if not can_place and x - obstacles[idx - 1] >= sz:
#                 can_place = True

#             result.append(can_place)

#     return result

# queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
# print(can_place_blocks(queries))

