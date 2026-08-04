def maximum_subarray_sum(nums):
    n = len(nums)  
    if n == 0:
        return 0

    p1 = [0] * (n + 1)
    for i in range(1, n + 1):
        p1[i] = max(p1[i - 1] + nums[i - 1], nums[i - 1], 0)
        
    max_sum = p1[1] if n > 0 else 0
    for i in range(1, n + 1):
        if p1[i] > max_sum:
            max_sum = p1[i]

    return max_sum


def maximum_subarray_sum_optimized(nums):
    n = len(nums)
    if n == 0:
        return 0

    T = float('-inf')  # Handles arrays with all negative numbers correctly
    prev = 0
    for i in range(n):
        current = max(prev + nums[i], nums[i])
        prev = current
        T = max(T, current)

    return T  # Fixed: changed 'Ti' to 'T'