# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/
#
# Houses are arranged in a circle (first and last are neighbors).
#
# Example: nums = [2, 3, 2] -> 3


def _rob_linear(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        rob1, rob2 = rob2, max(rob1 + n, rob2)
    return rob2


def rob_circular(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(_rob_linear(nums[1:]), _rob_linear(nums[:-1]))


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = rob_circular(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
