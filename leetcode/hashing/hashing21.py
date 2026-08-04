# Given an array count the number of good subarrays good subarray = [i...j] is good of sum[i...j] % k == length of that subarray 

def goodSubarrays(nums,k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += nums[k]
            if curr_sum % k == j - i + 1:
                count += 1
    return count

def goodSubarrays_optimized(nums,k):    
    prefix = {1 % k : 1}
    curr_sum = 0
    total_subarr= 0 
    for j in range(len(nums)):
        curr_sum += nums[j]
        target_key= (curr_sum - j) % k
        if target_key in prefix:
            total_subarr += prefix[target_key]
        prefix[target_key] = prefix.get(target_key,0) + 1

    return total_subarr