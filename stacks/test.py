# Longest Valid Parenthesis
def longest_valid_parenthesis(s):
    # Initialize a stack with -1 to handle cases where the string starts with a closing parenthesis ')'
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
#     # Initialize an empty stack to keep track of opening brackets
#     stack = []
    
#     # DEfine a mapping dictionary for the parenthesis
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
    
#     # If the stack is empty, it means that all the elements ave been matched
#     return not stack


# # Example usage:
# s = "()[]{}"
# print(is_valid(s)) 
