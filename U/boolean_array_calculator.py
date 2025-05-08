"""
Given array a[], b[], c[] and signs[], need to return a boolean array based on condition a[i] signs[i] b[i] = c[i]     
"""

def evaluate_conditions(a, b, c, signs):
    result = []
    
    for i in range(len(a)):
        if signs[i] == '+':
            result.append(a[i] + b[i] == c[i])
        elif signs[i] == '-':
            result.append(a[i] - b[i] == c[i])
        elif signs[i] == '*':
            result.append(a[i] * b[i] == c[i])
        elif signs[i] == '/':
            if b[i] == 0:
                result.append(False)            
            result.append(a[i] / b[i] == c[i])
            
        else:
            result.append(False)
    
    return result

# Input arrays
a = [10, 8, 6]
b = [5, 2, 3]
c = [15, 4, 18]
signs = ["+", "*", "*"]

# Evaluate conditions
result = evaluate_conditions(a, b, c, signs)

# Output the result
print(result)


# def calculate(s):
#     stack = []
    

# s = " 2-1 + 2 "
# print(calculate(s))