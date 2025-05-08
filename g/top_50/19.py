# def justify_line(line, line_length, maxWidth):
#     if len(line) == 1:
#         # If there is only one word, left justify it
#         return line[0] + ' ' * (maxWidth - line_length)
    
#     # Calculate total spaces and gaps
#     total_spaces = maxWidth - line_length
#     gaps = len(line) - 1
#     spaces_per_gap = total_spaces // gaps
#     extra_spaces = total_spaces % gaps
    
#     justified_line = []
#     for i in range(len(line) - 1):
#         justified_line.append(line[i])
#         justified_line.append(' ' * (spaces_per_gap + (1 if i < extra_spaces else 0)))
        
#     justified_line.append(line[-1])
#     return ''.join(justified_line)


# def left_justify(line, maxWidth):
#     return ' '.join(line) + ' ' * (maxWidth - len(' '.join(line)))



def max_sum(arr):
    n = len(arr)
    
    s0, total_sum = 0, 0
    
    for i in range(n):
        s0 += i * arr[i]
        total_sum += arr[i]
        
    max_sum_val = s0
    
    current_sum = s0
    for i in range(1, n):
        current_sum = current_sum + total_sum - (n * arr[n - 1])
        max_sum_val = max(max_sum_val, current_sum)
    
    return max_sum_val