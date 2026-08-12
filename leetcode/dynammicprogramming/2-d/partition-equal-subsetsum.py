# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
#
# Return true if array can be partitioned into two subsets with equal sum.
#
# Example: nums = [1, 5, 11, 5] -> True


def can_partition(nums: list[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    memo = {}

    def dfs(start_index: int, current_sum: int) -> bool:
        if current_sum == target:
            return True
        if current_sum > target or start_index >= len(nums):
            return False
        state = (start_index, current_sum)
        if state in memo:
            return memo[state]
        memo[state] = dfs(start_index + 1, current_sum + nums[start_index]) or dfs(
            start_index + 1, current_sum
        )
        return memo[state]

    return dfs(0, 0)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([1, 1], True),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = can_partition(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
