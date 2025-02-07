from collections import Counter

def intersect(nums1, nums2):
    counts1, counts2 = Counter(nums1), Counter(nums2)
    
    intersection = []
    for element in counts1:
        if element in counts2:
            intersection.extend([element] * min(counts1[element], counts2[element]))
    
    return intersection

# Example usage:
nums1 = [4, 9, 5, 9]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))