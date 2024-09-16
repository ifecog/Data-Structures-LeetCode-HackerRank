from collections import defaultdict, deque

def find_order(num_courses, prerequisites):
    """There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    Args:
        num_courses (int): the number of courses to be taken
        prerequisites (array): an array of courses and their prerequisites
    """
    
    # This is solved using Kahn's Algorithm (BFS)
    #  1. Build the graph
    
    # Store the graph as an adjacency list
    adj_list = defaultdict(list)
    
    # Initiate an in_degree array to store hpw many prerequisites each course has
    in_degree = [0] * num_courses
    
    for course, pre in prerequisites:
        adj_list[pre].append(course)
        in_degree[course] += 1
        
    # Initialize a queue with all courses having an in_degree of 0 (meaning no prerequisites)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    
    # Initialize an empty list to store the final course ordering
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        # Process each neighbor and reduce thrie in_degree
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            
            # If the dependent course (neighbor) has n prerequisite, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # If all the courses have been processed, return the order list, else return an empty list
    return order if len(order) == num_courses else []
    
    
    
# Example usage
numCourses = 2
prerequisites = [[1, 0]]
print(find_order(numCourses, prerequisites))  # Output: [0, 1]