# Find the largest / smallest subarray  == k

def largest_subarray_sum_k(nums, k):
    max_len = 0
    res = (-1, -1)
    n = len(nums)

    for i in range(n):
        csum = 0
        for j in range(i, n):
            csum += nums[j]  # Fixed: added nums[j] instead of nums[i]
            # Check if sum equals k and length is greater than max_len
            if csum == k and (j - i + 1) > max_len:
                max_len = j - i + 1
                res = (i + 1, j + 1)  # Storing 1-based indices as per your original code

    return res


def largest_subarray_sum_k_optimized(nums, k):
    sum_index_map = {0: 0}
    current_sum = 0
    max_len = 0
    res = (-1, -1)
    
    for i in range(len(nums)):
        current_sum += nums[i]
        
        if (current_sum - k) in sum_index_map:
            length = i + 1 - sum_index_map[current_sum - k]
            if length > max_len:
                max_len = length
                res = (sum_index_map[current_sum - k] + 1, i + 1)
                
        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i + 1
            
    return res