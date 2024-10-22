def min_available_duration(slots1, slots2, duration):
    """Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

    If there is no common time slot that satisfies the requirements, return an empty array.

    The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

    It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1

    Args:
        slot1 (int): a list of time slot pairs
        slot2 (int): a list of time slot pairs
        duration (int): set duration
    """
    
    slots1.sort()
    slots2.sort()
    
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        
        if start - end >= duration:
            return [start, start + duration]
        
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    
    return []
       
    
# Example usage:
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
print(min_available_duration(slots1, slots2, duration))


# slots1 = [[10,50],[60,120],[140,210]]
# slots2 = [[0,15],[60,70]]
# duration = 12
# print(min_available_duration(slots1, slots2, duration))