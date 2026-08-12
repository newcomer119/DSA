# 494. Target Sum
# https://leetcode.com/problems/target-sum/
#
# Assign + or - to each number. Count ways to reach target.
#
# Example: nums = [1,1,1,1,1], target = 3 -> 5


def find_target_sum_ways(nums: list[int], target: int) -> int:
    dp = {}

    def backtrack(i: int, total: int) -> int:
        if i == len(nums):
            return 1 if total == target else 0
        if (i, total) in dp:
            return dp[(i, total)]
        dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(i + 1, total - nums[i])
        return dp[(i, total)]

    return backtrack(0, 0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([1, 0], 1, 2),
    ]
    passed = 0
    for nums, target, exp in TESTS:
        got = find_target_sum_ways(nums, target)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
