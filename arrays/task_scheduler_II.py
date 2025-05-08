def taskSchedulerII(tasks, space):
    """
    You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

    You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

    Each day, until all tasks have been completed, you must either:

    Complete the next task from tasks, or
    Take a break.
    Return the minimum number of days needed to complete all tasks.

    Args:
        tasks (array): An array of tasks to be completed
        space (int): An integer value representing space

    Returns:
        int: Minimum number of days needed to complete all tasks.
    """
    
    # Use an hash map (dictionary) to store the last day each task was completed 
    last_done = {}
    day = 0
    
    for task in tasks:
        day += 1
        
        if task in last_done:
            min_available_day = last_done[task] + space + 1
            
            if day < min_available_day:
                day = min_available_day
                
        last_done[task] = day
        
    return day


# Example usage:
tasks = [1, 2, 1, 2, 3, 1]  
space = 3
print("Minimum days to complete all tasks:", taskSchedulerII(tasks, space))