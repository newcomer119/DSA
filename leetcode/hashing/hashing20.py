# count subarrays with xor


def subArraysXor(arr,k):
    n = len(arr)
    count = 0
    for i in range(n):
        curr_xor = 0
        for j in range(i, n):
            curr_xor ^= arr[j]
            if curr_xor == k:
                count += 1

    return count


def subArraysXor_optimized(nums,k):
    prefix = {0 : 1}
    curr_xor = 0
    total_subarr = 0
    for num in nums:
        curr_xor ^= num
        target_xor = curr_xor ^ k
        if target_xor in prefix:
            total_subarr += prefix[target_xor]

        prefix[curr_xor] = prefix.get(curr_xor,0) + 1

    return total_subarr