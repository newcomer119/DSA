# Largest subarray sum == 0

def maxLength(nums):
    mL = 0
    n = len(nums)
    k = 0
    for i in range(len(nums)):
        for j in range(i , n):
            curr_sum += nums[i]
            if curr_sum == k and (j - i + 1) > mL:
                mL = j- i + 1

    return mL


def max_length_optimized(nums):
    sum_index = {0:0}
    curr_sum = 0
    k = 0
    max_len = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if (curr_sum-k) in sum_index:
            length = i + 1 - sum_index[curr_sum]
            if length > max_len:
                max_len = length

        if curr_sum not in sum_index:
            sum_index[curr_sum] = i + 1

    return max_len
