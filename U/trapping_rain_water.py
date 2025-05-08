from collections import deque, Counter, defaultdict


def waysToBuyPencils(total, cost1, cost2):
    ways = 0
    max_pens = total // cost1
    
    for pens in range(max_pens + 1):
        remaining = total - (pens * cost1)
        max_pencils = remaining // cost2
        
        ways +=(max_pencils + 1)
    
    return ways


# def trap(height):
#     if not height:
#         return 0
    
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]
    
#     water_trapped = 0
    
#     while left < right:
#         if left_max < right_max:
#             left += 1
            
#             left_max = max(left_max, height[left])
#             water_trapped += left_max - height[left]
            
#         else:
#             right -= 1
            
#             right_max = max(right_max, height[right])
#             water_trapped += right_max - height[right]
    
#     return water_trapped

# # Example usage
# length = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(length))


