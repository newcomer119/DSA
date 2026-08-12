# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
#
# Robot moves only right/down on m x n grid from top-left to bottom-right.
#
# Example: m = 3, n = 7 -> 28


def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[m - 1][n - 1]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(3, 7, 28), (3, 2, 3), (1, 1, 1)]
    passed = 0
    for m, n, exp in TESTS:
        got = unique_paths(m, n)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {m}x{n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
