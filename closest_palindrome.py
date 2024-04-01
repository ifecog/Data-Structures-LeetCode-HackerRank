def closest_palindrome(n):
    """Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one. The closest is defined as the absolute difference minimized between two integers.

    Args:
        n (str): a string of characters
    """
    
    # conversion to int for the purpose of iteration
    n = int(n)
    
    # nested function to determine palindrome status
    def is_palindrome(s):
        # return s == ''.join(reversed(s))
        return s == s[::-1]
    
    
    # nested function to determine nearest smaller palindrome
    def get_smaller_palindrome(x):
        x -= 1
        while x > 0 and not is_palindrome(str(x)):
            x -= 1
        
        return x
    
    
    # nested function to determin nearest higher palindrome
    def get_higher_palindrome(x):
        x += 1
        while True:
            if is_palindrome(str(x)):
                return x
            x += 1
            
    # assign variables for smaller and higher palindromes
    smaller_palindrome = get_smaller_palindrome(n)
    higher_palindrome = get_higher_palindrome(n)
    
    return str(smaller_palindrome) if abs(n - smaller_palindrome) <= abs(higher_palindrome - n) else str(higher_palindrome)


# Example usage:
n = "1234"
output = closest_palindrome(n)
print(output)
            