def remove_digits(s):
    """
    You are given a string s.

    Your task is to remove all digits by doing this operation repeatedly:

    Delete the first digit and the closest non-digit character to its left.
    Return the resulting string after removing all digits.

    Args:
        s (string): A string of charcters
    """
    
    stack = []
    
    for char in s:
        if char.isdigit():
            if stack and not stack[-1].isdigit():
                stack.pop()
                
        else:
            stack.append(char)
    
    return ''.join(stack)

# Example Usage
s = "a1bc2d3ef45"
result = remove_digits(s)
print(result)


            