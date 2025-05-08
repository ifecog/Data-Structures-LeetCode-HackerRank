def longest_valid_parenthesis(s):
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)
    
    return max_length

    
# Example usage:
s = "(()())"
print(longest_valid_parenthesis(s)) 


def is_valid(s):
    stack = []
    
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in mapping:
            coresponding_element = stack.pop() if stack else '#'
            
            if mapping[char] != coresponding_element:
                return False
            
        else:
            stack.append(char)
            
    return not stack

s = "()[]{}"
print(is_valid(s)) 

    