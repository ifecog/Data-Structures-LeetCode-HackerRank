def binary_search(list, n):
    """Given an array of integer nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target esists, then return its index, otherwise return -1. You must write an algorithm with O(log n) runtime complexity

    Args:
        list (integers): a sorted array of integers
        n (int): the target to be searchd in the list.
    """
    
    # initialize the lower boundary, upper boundary and middle for the list
    lb, ub, mid = 0, len(list) - 1, 0
    step = 0
    
    while lb <= ub:
        print('step', step, ':', str(list[lb:ub+1]))
        step += 1 # step increment until element is located
        
        # get the midpoint
        mid = (lb + ub) // 2
        
        # set conditions for search execution
        if n == list[mid]:
            return mid
        elif n > list[mid]:
            lb = mid + 1
        else:
            ub = mid - 1
                
    return -1


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(test_list)
target = int(input('Target element?'))

print('Target Location:', binary_search(test_list, target))