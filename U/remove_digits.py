
"""
You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
"""

def remove_digits(s):
    stack = []
    
    for char in s:
        if char.isdigit():
            if stack:
                stack.pop()
        
        else:
            stack.append(char)
    
#     return ''.join(stack)

# # Example Usage
# s = "a1bc2d3ef45"
# result = remove_digits(s)
# print(result)


from collections import deque

def letter_combinations(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    queue = deque([''])
    
    for digit in digits:
        for _ in range(len(queue)):
            combination = queue.popleft()
            
            for letter in phone_map[digit]:
                queue.append(combination + letter)
                
    return list(queue)


def letter_combo(digits):
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(partial_combination, next_digits):
        if not next_digits:
            result.append(partial_combination)
        else:
            for letter in phone_map[next_digits[0]]:
                backtrack(partial_combination + letter, next_digits[1:])
                
    backtrack('', digits)
    
    return result


# Example usage
number = '56'
print(letter_combo(number))
