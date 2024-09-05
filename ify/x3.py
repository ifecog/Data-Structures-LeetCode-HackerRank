# def fibonacci_recursive(n):
#     if n <= 0:
#         return 'Number must be greater than 0'
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iteration(n):
    if n <= 0:
        return 'Number must be greater than 0'
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        
        return fib_sequence[-1]
    
    
a = 8
print(fibonacci_iteration(a))

# Example usage
# for i in range(1, 9):
#     print(fibonacci_recursive(i), end=' ')