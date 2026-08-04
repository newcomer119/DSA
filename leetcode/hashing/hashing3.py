# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
#
# Return true if there are two equal values at indices i and j with |i - j| <= k.
#
# Example:
# nums = [1, 2, 3, 1], k = 3 -> True
# nums = [1, 0, 1, 1], k = 1 -> True
# nums = [1, 2, 3, 1, 2, 3], k = 2 -> False


def contain_nearby_duplicate(nums: list[int], k: int) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and j - i <= k:
                return True
    return False


def contain_nearby_duplicate_hashing(nums: list[int], k: int) -> bool:
    num_indices = {}
    for i, num in enumerate(nums):
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
    return False


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]
    passed = 0
    for nums, k, exp in TESTS:
        got = contain_nearby_duplicate_hashing(nums, k)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] nums={nums}, k={k} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
