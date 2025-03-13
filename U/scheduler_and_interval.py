def merged_intervals(intervals):
    intervals.sort(key=lambda i: i[0])
    
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
            
        merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = merged_intervals(intervals)
print(result)


def min_available_duration(slots1, slots2, duration):
    slots1.sort(), slots2.sort()
    
    i = j = 0
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