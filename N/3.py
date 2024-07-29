# def palindrome(n):
#     """Find the next Palindrome number given a base number

#     Args:
#         n (int): given base number
        
#     Returns:
#         n1 (int), the next palindrome number to n
#     """
    
#     while True:
#         n = str(n)
#         n_reverse = n[::-1]
        
#         if n == n_reverse:
#             return n
        
#         else:
#             n = int(n)
#             n += 1
            

# # Example usage
# number = int(input('Insert the number: '))
# print('The next palindrome number after', number, 'is', palindrome(number))


def closest_palindrome(n):
    # Convert to int for the purpose of iteration
    n = int(n)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    
    def get_smaller_palindrome(x):
        x -= 1
        while x > 0 and not is_palindrome(str(x)):
            x -= 1
        
        return x
    
    
    def get_higher_palindrome(x):
        x += 1
        while True:
            if is_palindrome(str(x)):
                return x
            x += 1
            
    smaller_palindrome = get_smaller_palindrome(n)
    higher_palindrome = get_higher_palindrome(n)
    
    return str(smaller_palindrome) if abs(n - smaller_palindrome) <= abs(n - higher_palindrome) else str(higher_palindrome)


# Example usage:
n = "12345"
output = closest_palindrome(n)
print(output)
