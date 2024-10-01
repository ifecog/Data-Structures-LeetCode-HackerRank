from collections import defaultdict, deque

# # Course Schedule I & II
# def find_order(num_courses, prerequisites):
#     # This is solved using Kahn's algorithm
#     # 1. Build the graph (Store the graph as an adjacency list)
#     adj_list = defaultdict(list)
    
#     # In-degree array to store how many prerequisites each course has
#     in_degree = [0] * num_courses
    
#     for course, pre in prerequisites:
#         adj_list[pre].append(course)
#         in_degree[course] += 1
        
#     # 2. BFS
#     # Initialize a queue with all courses having an in_degree of 0 (meaning no prerequisites)
#     queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
#     # Empty list to store the final course ordering
#     order = []
    
#     while queue:
#         course = queue.popleft()
#         order.append(course)
        
#         # Process wach neighbor and reduce the in-degree
#         for neighbor in adj_list[course]:
#             in_degree[neighbor] -= 1
            
#             # If the dependent course (neighbor) has no prerequisite, add it to the queue
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
    
#     # IF all the coutses hae been processed, return the order list, else, return an emply list
#     return order if len(order) == num_courses else []

# # Example usage
# numCourses = 2
# prerequisites = [[1, 0]]
# print(find_order(numCourses, prerequisites))  # Output: [0, 1]



# Course Schedule III Solution
import heapq

def schedule_course(courses):
    courses.sort(key=lambda i: i[1])
    
    # Max heap to store the duration of courses taken
    max_heap = []
    current_time = 0
    
    for duration, last_day in courses:
        # Add the durations to the heap
        # -ve duration is used because in Python, the default heap is min heap
        heapq.heappush(max_heap, -duration)
        current_time += duration
        
        if current_time > last_day:
            # Remove the longest duration (which is at the root of the heap)
            longest_duration = -heapq.heappop(max_heap)
            current_time -= longest_duration
    
    return len(max_heap)


# Test the example case
courses = [[5,5], [4,6], [2,6]]
print(schedule_course(courses))

        


# # Course Schedule III (inadequate solution)
# def schedule_course(courses):
#     courses.sort(key=lambda i: i[1])
    
#     time, count = 0, 0
#     for duration, last_day in courses:
#         if time + duration <= last_day:
#             time += duration
#             count += 1
    
#     return count

# courses = [[5,5], [4,6], [2,6]]
# print(schedule_course(courses))


# import heapq

# heap = [4, 8, 2, 6, 7, 1]
# heapq.heapify(heap)
# print(heap)

# k_largest = heapq.nsmallest(3, heap)
# print(k_largest)