# Pruning Template
# function dfs(start_index, path):
#     if is_leaf(start_index):
#         report(path)
#         return
#     for edge in get_edges(start_index):
#         # prune if needed
#         if not is_valid(edge):
#             continue
#         path.add(edge)
#         dfs(start_index + 1, path)
#         path.pop()

# 51. N-Queens
# https://leetcode.com/problems/n-queens/

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration, where 'Q' and '.'
# indicate a queen and an empty space, respectively.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

# Example 2:
# Input: n = 1
# Output: [["Q"]]

# Constraints:
# 1 <= n <= 9


def solve_n_queens(n: int) -> list[list[str]]:
    res = []

    def is_safe(row: int, col: int, path: list[int]) -> bool:
        for r, c in enumerate(path):
            if c == col:
                return False
            if abs(row - r) == abs(col - c):
                return False
        return True

    def build_board(path: list[int]) -> list[str]:
        board = []
        for col in path:
            row = ["."] * n
            row[col] = "Q"
            board.append("".join(row))
        return board

    def dfs(row: int, path: list[int]) -> None:
        if row == n:
            res.append(build_board(path))
            return

        for col in range(n):
            if not is_safe(row, col, path):
                continue
            path.append(col)
            dfs(row + 1, path)
            path.pop()

    dfs(0, [])
    return res


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (1, [["Q"]]),
        (2, []),
        (4, [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ]),
    ]
    passed = 0
    for n, exp in TESTS:
        got = sorted(solve_n_queens(n))
        expected = sorted(exp)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {len(got)} board(s)")
    print(f"\n{passed}/{len(TESTS)} passed")
