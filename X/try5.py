def merged_intervals(intervals):
    # Sort the array of intervals based on the starting point
    intervals.sort(key=lambda i : i[0])
    
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
