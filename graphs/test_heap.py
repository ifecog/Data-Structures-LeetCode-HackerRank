import heapq

def schedule_course(courses):
    # Sort the courses ccording to their last day
    courses.sort(key=lambda i: i[1])
    
    max_heap = []
    current_time = 0
    
    for duration, last_day in courses:
        heapq.heappush(max_heap, -duration)
        current_time += duration
        
        if current_time > last_day:
            # Remove the longest duration (which is at the root of the heap)
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
    
    return len(max_heap)

    
#     count = 0
#     time = 0
    
#     for duration, last_day in courses:
#         if time + duration <= last_day:
#             time += duration
#             count += 1
    
#     return count

# Test the example case
courses = [[5,5], [4,6], [2,6]]
print(schedule_course(courses))