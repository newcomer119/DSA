# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
#
# Return length of longest strictly increasing path (4 directions).
#
# Example: [[9,9,4],[6,6,8],[2,1,1]] -> 4


def longest_increasing_path(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = {}

    def dfs(r: int, c: int, preval: int) -> int:
        if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= preval:
            return 0
        if (r, c) in dp:
            return dp[(r, c)]
        res = 1 + max(
            dfs(r + 1, c, matrix[r][c]),
            dfs(r - 1, c, matrix[r][c]),
            dfs(r, c + 1, matrix[r][c]),
            dfs(r, c - 1, matrix[r][c]),
        )
        dp[(r, c)] = res
        return res

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, -1)
    return max(dp.values()) if dp else 1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
    ]
    passed = 0
    for matrix, exp in TESTS:
        got = longest_increasing_path(matrix)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] matrix -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
