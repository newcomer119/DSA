# Find count of shortest largest subarray with sum equal to k
def shortest_subarray_sum_k(nums, k):
    n =len(nums)
    max_length = 0
    count = 0
    for start in range(n):
        sum = 0
        for end in range(start , n):
            sum += nums[end]
            if sum == k:
                length = end - start + 1
                if length > max_length:
                    max_length = length
                    count = 1
                elif length == max_length:
                    count += 1
    return count

def shortest_subarray_sum_k_optimized(nums, k):
    mp1 = {0 : 0}
    mp2 = {0 : 0}
    pSum = 0
    maxLength = 0
    minLength = float('inf')
    n = len(nums)

    for j in range(1, n + 1):
        pSum  += nums[j - 1]
        target = pSum - k
        
        if target in mp1:
            i = mp1[target] + 1  # Fixed: changed mp to mp1
            currLength = j - i + 1
            if currLength > maxLength:  
                maxLength = currLength

        if target in mp2:
            i = mp2[target] + 1
            currLength = j - i + 1
            if currLength < minLength:
                minLength = currLength

        if pSum not in mp1:
            mp1[pSum] = j
        mp2[pSum] = j

    return maxLength, minLength