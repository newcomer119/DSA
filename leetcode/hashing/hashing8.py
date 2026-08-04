# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# GFG: https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/
#
# Count the number of contiguous subarrays whose sum equals k.
#
# Example:
# nums = [1, 1, 1], k = 2 -> 2
# nums = [1, 2, 3], k = 3 -> 2


def count_subarray_sum_brute(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count


def optimized_count(arr: list[int], k: int) -> int:
    prefix_sum = {0: 1}
    current_sum = 0
    count = 0
    for num in arr:
        current_sum += num
        if (current_sum - k) in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
    ]
    passed = 0
    for nums, k, exp in TESTS:
        got = optimized_count(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] nums={nums}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
