def longest_valid_parenthesis(s):
    """Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parenthesis substring.

    Args:
        s (string): a string of characters '(' and ')'
    """
    
    # Initialize a stack with -1
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
