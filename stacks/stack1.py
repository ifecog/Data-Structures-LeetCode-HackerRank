def is_valid(s):
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Args:
        words (string): a sting of characters
        k (_type_): _description_
        
    Solution:
    
    Initialize an empty stack.
    
    Define a dictionary mapping that maps each closing bracket to its corresponding opening bracket.

    Iterate through each character in the input string s.

    If the character is a closing bracket, check if the top element of the stack matches the corresponding opening bracket. If they don't match, return False, indicating that the string is not valid.

    If the character is an opening bracket, push it onto the stack.

    After processing all characters, if the stack is empty, return True (indicating that all brackets are properly matched and closed). If the stack is not empty, return False.
    """
    
    # Inialize an empty stack
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
    
        # print(stack)
    
    return not stack

# Example usage:
s = "()[]{}"
print(is_valid(s)) 

# a = "(]"
# print(is_valid(a))