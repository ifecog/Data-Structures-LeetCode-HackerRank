from collections import Counter

def intersect(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

    Args:
        nums1 (int): An array of integers
        nums2 (int): An array of integers

    Returns:
        int: An array of the intersection
    """

    count1, count2 = Counter(nums1), Counter(nums2)
    intersection = []
    
    for element in count1:
        if element in count2:
            intersection.extend([element] * min(count1[element], count2[element]))
            
    return intersection    


# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))