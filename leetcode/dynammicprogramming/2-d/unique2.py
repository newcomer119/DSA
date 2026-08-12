# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
#
# Same as unique paths, but grid has obstacles (1 = obstacle, 0 = empty).
#
# Example: [[0,0,0],[0,1,0],[0,0,0]] -> 2


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    rows, cols = len(obstacle_grid), len(obstacle_grid[0])
    if obstacle_grid[0][0] == 1 or obstacle_grid[rows - 1][cols - 1] == 1:
        return 0

    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = 1

    for row in range(rows):
        for col in range(cols):
            if obstacle_grid[row][col] == 1:
                dp[row][col] = 0
                continue
            if row > 0:
                dp[row][col] += dp[row - 1][col]
            if col > 0:
                dp[row][col] += dp[row][col - 1]
    return dp[rows - 1][cols - 1]


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[1, 0]], 0),
    ]
    passed = 0
    for grid, exp in TESTS:
        got = unique_paths_with_obstacles(grid)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] grid -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
