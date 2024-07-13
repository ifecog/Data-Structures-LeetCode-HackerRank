def is_valid(s):
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Args:
        words (string): a sting of characters
        k (_type_): _description_
    """
    
    # Inialize an empty stack to keep track of opening brackets
    stack = []
    
    # Define a mapping dictonary
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            
            if mapping[char] != top_element:
                return False
        
        else:
            stack.append(char)
        
    return not stack

# Example usage:
s = "()[]{}"
print(is_valid(s)) 

# a = "(]"
# print(is_valid(a))