# def closest_palindrome(n):
#     # Convert n to int for the purpose of incrementing
#     n = int(n)
    
#     def is_palindrome(s):
#         return s == s[::-1]
    
    
#     def get_smaller_palindrome(x):
#         x -= 1
#         while x > 0 and not is_palindrome(str(x)):
#             x -= 1
        
#         return x
    
    
#     def get_higher_palindrome(x):
#         x += 1
#         while True:
#             if is_palindrome(str(x)):
#                 return x
#             x += 1
    
#     smaller_palindrome = get_smaller_palindrome(n)
#     higher_palindrome = get_higher_palindrome(n)
    
#     return str(smaller_palindrome) if abs(n - smaller_palindrome) <= abs(higher_palindrome - n) else str(higher_palindrome)


# # Example usage:
# n = "12345"
# output = closest_palindrome(n)
# print(output)



# def is_palindrome(s):
#     return s == s[::-1]

# # Example usage
# a = 'etate'
# print(is_palindrome(a))


def palindrone(n):
    while True:
        n = str(n)
        if n == n[::-1]:
            return n
        else:
            n = int(n)
            n += 1


# Example usage
number = 565372
print(palindrone(number))