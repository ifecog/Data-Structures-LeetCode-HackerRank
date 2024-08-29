# Longest Valid Parenthesis
def longest_valid_parenthesis(s):
    # Initialize a stack with -1 to handle the case where the string starts with a closing parenthesis ')'
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


# # Valid Parenthesis
# def is_valid(s):
#     # Initiate an empty stack to keep track of opening brackets
#     stack = []
    
#     # Define a mapping dictionary with closing brackets as keys and opening brackets as values
#     mapping = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
    
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
            
#             if mapping[char] != top_element:
#                 return False
        
#         else:
#             stack.append(char)


# # Example usage:
# s = "()[]{}"
# print(is_valid(s))  
