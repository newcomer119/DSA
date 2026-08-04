# Subarray with sum k 

def countSubarray(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += nums[k]
            if curr_sum == k:
                count += 1
    return count

def countSubarray_optimized(nums, k):
    prefix = {0 : 1}
    curr_sum = 0
    total_subarr =0 
    for num in nums:
        curr_sum += num
        if (curr_sum - k) in prefix:
            total_subarr += prefix[curr_sum - k]

        prefix[curr_sum] = prefix.get(curr_sum,0) + 1


    return total_subarr