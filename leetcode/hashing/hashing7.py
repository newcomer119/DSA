# find the sum of range [l........r] when (l <= r) using prefix sum
def brute_force_sum(nums,l,r):
    return sum(nums[l:r+1])

def prefix_sum(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix[i] = prefix[i-1] + nums[i-1]

    return prefix 

def optimised_sum(prefix,l,r):
    return prefix[r] - prefix[l - 1]

