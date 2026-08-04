# check if there is any equal two numbers in array at a distance less than or equal to k ?

def contain_nearby_duplicate(nums, k):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and j <= i + k:
                return True 

    return False 


def contain_nearby_duplicate_hashing(nums, k):
    num_indices = {}
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True 

        num_indices[num] = i

    return False 