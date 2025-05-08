"""Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval()."""

def calculate(s):
    stack = [] # To handle parenthesis
    current_num = 0
    sign = 1 # 1 for positice, -1 for negative
    result = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        
        elif char == '+':
            result += sign * current_num
            current_num = 0
            sign = 1
        
        elif char == '-':
            result += sign * current_num
            current_num = 0
            sign = -1
            
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
            
        elif char == ')':
            result += sign * current_num
            current_num = 0
            result *= stack.pop()
            result += stack.pop()
            
    # After processing all characters, add any remaining current_sum to the result
    result += sign * current_num
    
    return result

s = " 2-1 + 2 "
print(calculate(s))