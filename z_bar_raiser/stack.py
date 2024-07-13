# 1. Valid Parenthesis
def is_valid(s):
    # Initialize an empty stack to keep track of opening brackets
    stack = []
    
    # DEfine a mapping dictionary for each bracket pair
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            
            if bracket_map[char] != top_element:
                return False
        
        else:
            stack.append(char)
        
    return not stack

# Example usage
a = "(]"
print(is_valid(a))