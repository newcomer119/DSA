# Longest Consecutive sequence 


def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    nums.sort()
    n = len(nums)
    cs = 1
    ls = 1
    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            continue 

        if nums[i + 1] - nums[i] == 1:
            cs += 1
        else:
            cs = 1

        ls = max(ls, cs)

    return ls


def longest_consecutive_sequence_optimized(nums):
    if not nums:
        return 0

    num_set = set(nums)
    max_streak = 0
    for x in num_set:
        if x - 1 not in num_set:
            current_num = x
            current_streak = 1  # Fixed variable name
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1  # Fixed variable name
            max_streak = max(max_streak, current_streak)

    return max_streak