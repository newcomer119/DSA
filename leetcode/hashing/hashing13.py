# Determine the minimum number of steps to make all the piles equal in height 

from collections import Counter
def minimum_steps(piles):
    steps = 0
    while True:
        unique = sorted(list(set(piles)),reverse=True)
        if len(unique) <= 1:
            break

        large1 = unique[0]
        large2 = unique[1]

        for i in range(len(piles)):
            if piles[i] == large1:
                piles[i] = large2
                steps += 1
                break

    return steps



def minimum_steps_optimized(piles):
    # Count frequencies of each pile height
    freq = Counter(piles)
    
    # Sort the unique heights in descending order
    sorted_unique_heights = sorted(freq.keys(), reverse=True)
    
    steps = 0
    accumulated_piles = 0
    
    # Iterate through all heights except the smallest one
    for i in range(len(sorted_unique_heights) - 1):
        accumulated_piles += freq[sorted_unique_heights[i]]
        steps += accumulated_piles
        
    return steps