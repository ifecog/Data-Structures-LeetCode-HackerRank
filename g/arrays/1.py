def merge(intervals):
    intervals.sort(key=lambda i: i[0])
    
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] <= interval[0]:
            merged.append(interval)
        
        merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged

# Example usage
trys = [[1,3],[2,6],[8,10],[15,18]]
print(merge(trys))