# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/
#
# Find minimum sum path from top-left to bottom-right (right/down only).
#
# Example: [[1,3,1],[1,5,1],[4,2,1]] -> 7


def min_path_sum(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    for col in range(1, cols):
        dp[0][col] = dp[0][col - 1] + grid[0][col]
    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + grid[row][0]
    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
    return dp[rows - 1][cols - 1]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
    ]
    passed = 0
    for grid, exp in TESTS:
        got = min_path_sum(grid)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] grid -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
