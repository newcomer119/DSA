# Stable Subarray — Equal Boundary Values with Matching Interior Sum
# Practice problem — brute force with prefix-sum thinking.
#
# Count subarrays nums[i..j] (j > i) where:
#   nums[i] == nums[j]  AND  sum(nums[i+1 .. j-1]) == nums[i]
# For length-2 subarrays (j == i + 1), interior sum is 0.
#
# Example:
# nums = [0, 0] -> 1


def stable_subarray(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    for i in range(n):
        interior_sum = 0
        for j in range(i + 1, n):
            if j > i + 1:
                interior_sum += nums[j - 1]
            if nums[i] == nums[j] and interior_sum == nums[i]:
                count += 1
    return count


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([0, 0], 1),
        ([1, 2, 1], 0),
        ([9, 3, 6, 2, 3, 6, 9], 0),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = stable_subarray(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
