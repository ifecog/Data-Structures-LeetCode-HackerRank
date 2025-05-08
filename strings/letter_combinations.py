from collections import deque

def letter_combinations(digits):
    """Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Args:
        digit (str): the given integer wrapped in a string.
    """
    
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
    
    # Iterate through each digit in the input string
    for digit in digits:
        # Process all existing partial combinations
        for _ in range(len(queue)):
            partial_combination = queue.popleft()
            
            # Appeend each letter correspondidng to the current digit
            for letter in phone_map[digit]:
                queue.append(partial_combination + letter)
                
        return list(queue)
    
    
    # # Method: Recursion
    # result = []
    
    # # Backtracking function to generate combinations
    # def backtrack(combination, next_digits):
    #     if not next_digits:
    #         result.append(combination)
    #     else:
    #         for letter in phone_map[next_digits[0]]:
    #             backtrack(combination + letter, next_digits[1:])
                
    # backtrack('', digits)
    
    # return result

# Example usage
number = '56'
print(letter_combinations(number))