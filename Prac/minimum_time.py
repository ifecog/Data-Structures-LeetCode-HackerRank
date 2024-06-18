def minimum_time(time, totalTrips):
    """You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

    Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

    You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

    Args:
        time (array<int>): an array of integers representing time
        total_trips (int): least total trips completed
    """
    """
    Solution:
    
    Initialize left to 1 and right to the minimum time taken by any bus multiplied by totalTrips. This represents the range of possible minimum times required.
    
    Define a helper function can_complete_trips(max_time) that checks whether it's possible to complete totalTrips trips with the given maximum time max_time. It iterates through each bus's time and calculates how many trips can be completed within max_time.

    Perform binary search to find the minimum time required to complete at least totalTrips trips. At each step, calculate the midpoint mid of the range and check if it's possible to complete totalTrips trips within mid time. Adjust the range (left or right) accordingly.

    Once the binary search terminates (left is equal to right), return left, which represents the minimum time required to complete at least totalTrips trips.
    """
    
    left = 1
    # The maximum time needed if only the fastest bus was used to complete all trips
    right = min(time) * totalTrips
    
    # Helper function to determine if it is possible to complete the required number of trips within max_time
    def can_complete_trips(max_time):
        total_trips = 0
        for t in time:
            total_trips += max_time // t
        
        return total_trips >= totalTrips
    
    while left < right:
        mid = (left + right) // 2
        
        if can_complete_trips(mid):
            right = mid
        else:
            left = mid + 1
    
    # When left meets right, we have found the minimum time required
    return left
   
    
# Example usage:
time_period = [2, 3, 5]
total_trips_taken = 8
print(minimum_time(time_period, total_trips_taken))
