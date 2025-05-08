from collections import Counter

def leastInterval(tasks, n):
    """
    You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

    Return the minimum number of CPU intervals required to complete all tasks.

    Args:
        tasks (array): an array of tacks
        n (int): an interger number
    """
    
    task_counts = Counter(tasks)
    # Find the most frquent task
    max_freq = max(task_counts.values())
    # Count how many tasks have this frequency
    max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)
    
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)
    
    
# Example usage:
tasks = ["A", "A", "A", "B", "A", "B", "B", "B"]
n = 2
print("Minimum CPU intervals:", leastInterval(tasks, n))