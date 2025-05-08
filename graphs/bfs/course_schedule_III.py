import heapq

def schedule_course(courses):
    """There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

    You will start on the 1st day and you cannot take two or more courses simultaneously.

    Return the maximum number of courses that you can take.

    Args:
        courses (list): A list of tuples

    Returns:
        int: maximum number of courses that can be taken
    """
    
    # # Sort the courses by their last day
    # courses.sort(key=lambda i: i[1])
    
    # # Max heap to store the duration of courses taken
    # max_heap = []
    # current_time = 0
    
    # for duration, last_day in courses:
    #     # Add the durations to the heap
    #     # -ve duration is pushed because Python, by default, applies minimum heap
    #     heapq.heappush(max_heap, -duration)
    #     current_time += duration
        
    #     if current_time > last_day:
    #         # Remove the longest duration (which is at the root of the heap)
    #         longest_duration = -heapq.heappop(max_heap)
    #         current_time -= longest_duration
            
    # return len(max_heap)
    


    
    # Initialize current count and course time to 0
    time, count = 0, 0
    
    for duration, lastday in courses:
        if time + duration <= lastday:
            time += duration
            count += 1
    
    return count
    

# Test the example case
courses = [[5,5], [4,6], [2,6]]
print(schedule_course(courses))
