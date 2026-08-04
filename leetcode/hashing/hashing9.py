# Longest Subarray with Sum Equal to K
# GFG: https://www.geeksforgeeks.org/longest-sub-array-sum-k/
#
# Find the longest contiguous subarray with sum equal to k.
# Return 1-based start and end indices, or (-1, -1) if none exists.
#
# Example:
# nums = [1, -1, 5, -2, 3], k = 3 -> (1, 4)  # subarray [1, -1, 5, -2] has sum 3, length 4


def largest_subarray_sum_k(nums: list[int], k: int) -> tuple[int, int]:
    max_len = 0
    res = (-1, -1)
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k and (j - i + 1) > max_len:
                max_len = j - i + 1
                res = (i + 1, j + 1)
    return res


def largest_subarray_sum_k_optimized(nums: list[int], k: int) -> tuple[int, int]:
    sum_index_map = {0: 0}
    current_sum = 0
    max_len = 0
    res = (-1, -1)
    for i, num in enumerate(nums):
        current_sum += num
        if (current_sum - k) in sum_index_map:
            length = i + 1 - sum_index_map[current_sum - k]
            if length > max_len:
                max_len = length
                res = (sum_index_map[current_sum - k] + 1, i + 1)
        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i + 1
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, -1, 5, -2, 3], 3, (1, 4)),
        ([1, 2, 3], 6, (1, 3)),
        ([1, 2, 3], 10, (-1, -1)),
    ]
    passed = 0
    for nums, k, exp in TESTS:
        got = largest_subarray_sum_k_optimized(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] nums={nums}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
