# Count Subarrays with Sum Equal to K (duplicate practice of hashing8)
# https://leetcode.com/problems/subarray-sum-equals-k/
# GFG: https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/
#
# Count contiguous subarrays whose sum equals k.
#
# Example:
# nums = [10, 2, -2, -20, 10], k = -10 -> 3


def count_subarray(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count


def count_subarray_optimized(nums: list[int], k: int) -> int:
    prefix = {0: 1}
    curr_sum = 0
    total_subarr = 0
    for num in nums:
        curr_sum += num
        if (curr_sum - k) in prefix:
            total_subarr += prefix[curr_sum - k]
        prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
    return total_subarr


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([10, 2, -2, -20, 10], -10, 3),
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 7, 0),
    ]
    passed = 0
    for nums, k, exp in TESTS:
        got = count_subarray_optimized(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] nums={nums}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
