import heapq

def schedule_course(courses):
    courses.sort(key=lambda i: i[1])
    
    max_heap, current_time = [], 0
    
    for duration, lastday in courses:
        heapq.heappush(max_heap, -duration)
        current_time += duration
        
        if current_time > lastday:
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
            
    
    return len(max_heap)
    
# Test the example case
courses = [[5,5], [4,6], [2,6]]
print(schedule_course(courses))



# def schedule_course(courses):
#     courses.sort(key=lambda i: i[1])
    
#     time, count = 0, 0
#     for duration, lastday in courses:
#         if time + duration <= lastday:
#             time += duration
#             count += 1
    
#     return count