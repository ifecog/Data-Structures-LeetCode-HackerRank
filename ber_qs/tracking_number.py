# import string, random

# def generage_tracking_number(prefix='VWXYZ', sections=4, section_length=5):
#     part = [
#         ''.join(random.choices(string.ascii_uppercase + string.digits, k=section_length)) for _ in range(sections)
#     ]
    
#     return f"{prefix}-{'-'.join(part)}"
    

# print(generage_tracking_number())

def check_subarray_sum(nums, k):
    """
    Checks if there exists a subarray of `nums` with length at least 2 whose sum is a multiple of `k`.

    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

    Args:
        nums: A list of integers.
        k: An integer.

    Returns:
        True if such a subarray exists, False otherwise.
    """

    # Use a dictionary to store the remainder of prefix sums modulo k and their indices.
    # The key is the remainder and the value is the first index where that remainder was encountered.
    # Initialize with {0: -1} to handle cases where a subarray starting from index 0 is a multiple of k.
    prefix_mod = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        # Calculate the running sum.
        current_sum += num

        # If k is not zero, calculate the remainder when current_sum is divided by k.
        # This is crucial for checking multiples of k. If k is zero, we keep the raw sum.
        if k != 0:
            current_sum %= k

        # Check if we've seen this remainder before.
        if current_sum in prefix_mod:
            # If we've seen this remainder at an earlier index, it means the sum of elements
            # between that index and the current index is a multiple of k.
            # Check if the length of this subarray is at least 2.
            if i - prefix_mod[current_sum] >= 2:
                return True  # Found a valid subarray.

        else:
            # If this remainder is encountered for the first time, store it with its index.
            prefix_mod[current_sum] = i

    return False  # No valid subarray found.


# Example usage
nums = [23, 2, 4, 6, 7]
k = 6
print(check_subarray_sum(nums, k))  # Output: True

nums = [23, 2, 6, 4, 7]
k = 6
print(check_subarray_sum(nums, k)) # Output: True

nums = [23, 2, 6, 4, 7]
k = 13
print(check_subarray_sum(nums, k)) # Output: False

nums = [0,0]
k = 0
print(check_subarray_sum(nums, k)) # Output: True