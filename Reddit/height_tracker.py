def height_checker(heights):
    """A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].

    Args:
        heights (int): an integer of heights

    Returns:
        _type_: _description_
    """
    expected = sorted(heights)
    
    # # solution 1
    # count = 0
    # for i in range(len(heights)):
    #     if heights[i] != expected[i]:
    #         count += 1
            
    # solution 2
    count = sum(h1 != h2 for h1, h2 in zip(heights, expected))
    
    return count

# Example usage:
heights = [1,1,4,2,1,3]
result = height_checker(heights)
print(result) 