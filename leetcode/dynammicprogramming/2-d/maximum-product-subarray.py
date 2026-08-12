# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
#
# Find contiguous subarray with largest product.
#
# Example: nums = [2, 3, -2, 4] -> 6


def max_product(nums: list[int]) -> int:
    res = max(nums)
    curr_max, curr_min = 1, 1
    for n in nums:
        tmp = curr_max * n
        curr_max = max(curr_max * n, curr_min * n, n)
        curr_min = min(tmp, curr_min * n, n)
        res = max(res, curr_max)
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([2, -5, -2, -4, 3], 24),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = max_product(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
