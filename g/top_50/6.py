def findMinDifference(timePoints):
    minutes = []
    for time in timePoints:
        h, m = map(int, time.split(':'))
        minutes.append((h * 60) + m)
        
    minutes.sort()
    
    # Compare adjacent time points
    min_diff = float('inf')
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
    # Check the circular difference between the first and last time points
    min_diff = min(min_diff, (1440 + minutes[0]) - minutes[-1])
    
    return min_diff

# Test findMinDifference
timePoints = ["23:59", "00:00", "12:34"]
print("Minimum Time Difference:", findMinDifference(timePoints))