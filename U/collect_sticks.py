def collect_sticks(forest, bird):
    """
    You're given a forest array where 0 means empty space and +ve integer means a stick of size forest[i]. You're also give an index bird which denotes the init place of a bird in forest. Bird will always be at an empty index. The bird wants to build a nest of size 100 using the sticks in forest. In order to do so it follows the following algo:

    1. It flies to right until it finds a stick.

    2. Brings it back to its nest to build it.

    3. Then turns it direction and does the step 2.

    The bird keep following above until its nest of size 100 or greater is built. You need to return an array denoting the index of sticks that the bird picked to create the nest sorted in the order it picked them. Example: Input: forest=[10,50,0,100] bird=2 Output: [3]

    Args:
        forest (array): An array of integers
        bird (bird): The bird position 
    """
    
    n = len(forest)
    
    nest_size = 0
    picked_indices = []
    
    direction = 1 # 1 for right, -1 for left
    pos = bird
    
    while nest_size < 100:
        # If out of bounds, stop
        if not (0 <= pos < n):
            break
        
        while 0 <= pos < n and forest[pos] == 0:
            pos += direction
            
        # Collect the stick
        nest_size += forest[pos]
        picked_indices.append(pos)
        
        # Mark the stick as collected
        forest[pos] = 0
        
        # Switch direction
        direction *= -1
        
    return picked_indices

# Example usage
forest = [10, 50, 0, 100]
bird = 2
print(collect_sticks(forest, bird))


        