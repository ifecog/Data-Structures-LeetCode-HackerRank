from collections import deque

def depthSum(nestedList):
    """
    You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

    The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

    Return the sum of each integer in nestedList multiplied by its depth.

    Args:
        nestedList (int): a list of integers/lists
    """
    
    queue = deque([(nestedList, 1)])
    total = 0
    
    while queue:
        current_list, depth = queue.popleft()
        
        for element in current_list:
            if isinstance(element, int):
                total += element * depth
            else:
                queue.append((element, depth + 1))
    
    return total

nestedList = [1, [2, 2], [[3], 2], 1]
print(depthSum(nestedList))
    