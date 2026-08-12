# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/
#
# Return minimum jumps to reach the last index (guaranteed reachable).
#
# Example: nums = [2, 3, 1, 1, 4] -> 2


def jump(nums: list[int]) -> int:
    n = len(nums) - 1
    jumps = 0
    farthest = 0
    current_end = 0
    for i in range(n):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([1], 0),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = jump(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
