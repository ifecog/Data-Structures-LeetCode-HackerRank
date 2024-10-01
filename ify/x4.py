# Check if a number is a sum of the powers of 3
def check_powers_of_three(n):
    # Check if the base 3 representation of n contains only 0s and 1s
    while n > 0:
        if n % 3 == 2:
            return False
        
        n //= 3
    
    return True 


print(check_powers_of_three(12))  # True, because 12 = 9 + 3
print(check_powers_of_three(91))  # True, because 91 = 81 + 9 + 1


def is_power_of_four(n):
    if n <= 0:
        return False
    
    while n % 4 == 0:
        n //= 4
    
    return n == 1

# Example usage:
print(is_power_of_four(16))  # True, because 16 = 4^2
print(is_power_of_four(15))  # False, 15 is not a power of four