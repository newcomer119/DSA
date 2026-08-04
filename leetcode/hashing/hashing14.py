# Maximum distance between two elements 

def maxDistance(self,arr):
    freq = {}
    dist = 0
    for i , num in enumerate(arr):
        if num not in freq:
            freq[num] = i

        else:
            curr_dist = i - freq[num]
            if dist > curr_dist:
                dist = curr_dist

    return dist