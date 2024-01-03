def product_of_elements(nums):
    """Given an integer of array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]

    Args:
        nums (int): the given array

    Returns:
        int: an array of products
    """
    
    n = len(nums)
    
    left_products = [1] * n
    right_products = [1] * n
    
    # calculate the products the left of the element
    left_product = 1
    for i in range(1, n):
        left_product *= nums[i - 1]
        left_products[i] = left_product
        
    # calculate the products to the right of the element
    right_product = 1
    for i in range(n-2, -1, -1):
        right_product *= nums[i + 1]
        right_products[i] = right_product
        
    result = [left_products[i] * right_products[i] for i in range(n)]
    
    return result
    
        
# test code
array = [2, 4, 6, 8, 10]
result = product_of_elements(array)
print(result)