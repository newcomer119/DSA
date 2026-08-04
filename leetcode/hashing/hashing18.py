# Largest Subarray with Sum Zero
# GFG: https://www.geeksforgeeks.org/largest-subarray-with-0-sum/
# LeetCode (related): https://leetcode.com/problems/contiguous-array/
#
# Find the length of the longest contiguous subarray with sum equal to 0.
#
# Example:
# nums = [15, -2, 2, -8, 1, 7, 10, 23] -> 5  (subarray [-2, 2, -8, 1, 7])


def max_length(nums: list[int]) -> int:
    max_len = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == 0 and (j - i + 1) > max_len:
                max_len = j - i + 1
    return max_len


def max_length_optimized(nums: list[int]) -> int:
    sum_index = {0: 0}
    curr_sum = 0
    max_len = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum in sum_index:
            length = i + 1 - sum_index[curr_sum]
            if length > max_len:
                max_len = length
        if curr_sum not in sum_index:
            sum_index[curr_sum] = i + 1
    return max_len


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([1, 2, 3], 0),
        ([0, 0, 0], 3),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = max_length_optimized(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
