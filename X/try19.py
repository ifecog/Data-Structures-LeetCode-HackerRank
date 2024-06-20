def minimum_time(time, totalTrips):
    # This is solved using binary search
    left = 1
    # Set the right pointer to the maximum time needed for the rastest bus to complete all trips
    right = min(time) * totalTrips
    
    # Define a helper function tp determine if it is possible to complete the required number of trips within max_time
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
        
        return total_trips >= totalTrips
    
    # Binary search
    while left < right:
        mid = (left + right) // 2
        
        if can_complete_trips(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
    
    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
