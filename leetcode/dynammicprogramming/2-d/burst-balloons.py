# 312. Burst Balloons
# https://leetcode.com/problems/burst-balloons/
#
# Burst all balloons for max coins. Bursting i gives nums[i-1]*nums[i]*nums[i+1].
#
# Example: nums = [3, 1, 5, 8] -> 167


def max_coins(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    dp = {}

    def dfs(l: int, r: int) -> int:
        if l > r:
            return 0
        if (l, r) in dp:
            return dp[(l, r)]
        dp[(l, r)] = 0
        for i in range(l, r + 1):
            coins = nums[l - 1] * nums[i] * nums[r + 1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            dp[(l, r)] = max(dp[(l, r)], coins)
        return dp[(l, r)]

    return dfs(1, len(nums) - 2)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([3, 1, 5], 35),
    ]
    passed = 0
    for nums, exp in TESTS:
        got = max_coins(nums)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {nums} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
