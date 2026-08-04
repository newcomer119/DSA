# 53. Maximum Subarray — Prefix Sum Variant
# https://leetcode.com/problems/maximum-subarray/
#
# Same problem as hashing11.py, implemented with a prefix-sum style recurrence
# before reducing to Kadane's algorithm.
#
# Example:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6


def maximum_subarray_sum(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0

    p1 = [0] * (n + 1)
    for i in range(1, n + 1):
        p1[i] = max(p1[i - 1] + nums[i - 1], nums[i - 1], 0)

    return max(p1[1:]) if n > 0 else 0


def maximum_subarray_sum_optimized(nums: list[int]) -> int:
    if not nums:
        return 0

    best = float("-inf")
    prev = 0
    for num in nums:
        current = max(prev + num, num)
        prev = current
        best = max(best, current)
    return best


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-1], -1),
        ([-2, -1], -1),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = maximum_subarray_sum_optimized(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
