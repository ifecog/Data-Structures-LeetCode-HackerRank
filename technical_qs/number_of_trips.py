def minimum_time(time, totalTrips):
    # This is solved using the binary search approach
    left = 1
    right = min(time) * totalTrips
    
    def can_Complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
            
        return total_trips >= totalTrips
    
    while left < right:
        mid = (left + right) // 2
        
        if can_Complete_trips(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
