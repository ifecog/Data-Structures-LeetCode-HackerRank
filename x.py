# print('************Multiplication Table*************')
# num = int(input('Insert the number: '))
# for i in range(1, 13, 1):
#     result = num * i
#     print(f'{num} * {i} = {result}')

list = [element ** power for element in range(1, 5) for power in range(1, 4)]
print(list)

def first_non_repeating(nums):
    freq = {}
    
    for i, num in enumerate(nums):
        if num in freq:
            freq[num] = (freq[num][0] + 1, freq[num][1])
        else:
            freq[num] = (1, i)
    
    for num, (count, index) in freq.items():
        if count == 1:
            return index
    
    return None

# test
arr = [9, 4, 6, 8, 8, 2, 5, 8, 4, 6, 9]
print(first_non_repeating(arr))