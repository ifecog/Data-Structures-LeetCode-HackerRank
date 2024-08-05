def min_available_duration(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()
    
    # print('slot1:', slots1)
    # print('slot2:', slots2)
    
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        
        if start - end >= duration:
            return [start, start + duration]
        
        if slots1[i][i] < slots2[j][1]:
            i += 1
        else:
            j += 1
       
    return [] 
        
# Example usage:
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
print(min_available_duration(slots1, slots2, duration))

