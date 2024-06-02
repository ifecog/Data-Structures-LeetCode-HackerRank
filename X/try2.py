def closest_palindrome(n):
    n = int(n)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    
    def get_smaller_palindrome(x):
        x -= 1
        while x > 0 and not is_palindrome(str(x)):
            x -= 1
        return x
    
    
    def get_greater_palindrome(x):
        x += 1
        while True:
            if is_palindrome(str(x)):
                return x            
            x += 1
            
    smaller_palindrome = get_smaller_palindrome(n)
    greater_palindrome = get_greater_palindrome(n)
    
    return str(smaller_palindrome) if (n - smaller_palindrome) <= (greater_palindrome - n) else str(greater_palindrome)

# Example usage:
n = "12345"
output = closest_palindrome(n)
print(output)
