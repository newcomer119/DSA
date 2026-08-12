# 198. House Robber
# https://leetcode.com/problems/house-robber/
#
# Rob non-adjacent houses for maximum money.
#
# Example: nums = [1, 2, 3, 1] -> 4


def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev1, prev2 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prev1, prev2 = prev2, max(prev2, nums[i] + prev1)
    return prev2


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([5], 5),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = rob(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
