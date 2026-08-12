# 55. Jump Game
# https://leetcode.com/problems/jump-game/
#
# Return true if you can reach the last index from index 0.
# nums[i] = max jump length at position i.
#
# Example: nums = [2, 3, 1, 1, 4] -> True


def can_jump(nums: list[int]) -> bool:
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
        if max_reach >= len(nums) - 1:
            return True
    return True


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = can_jump(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
