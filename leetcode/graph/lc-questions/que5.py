# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.
# Example 1:
# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:
# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:
# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
# Constraints:
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:    
            return -1

        n = len(grid)
        def get_neighbors(r,c):
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if dr == 0 and dc == 0:
                        continue

                    nr,nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        yield(nr,nc)

        queue = deque([(0,0)])
        grid[0][0] = 1
        length = 1

        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == n- 1 and c == n -1:
                    return length 
                for nr,nc in get_neighbors(r, c):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr,nc))
            length += 1

        return -1

# --- Daily tests ---
if __name__ == "__main__":
    import copy

    sol = Solution()
    TESTS = [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ]
    passed = 0
    for grid, exp in TESTS:
        got = sol.shortestPathBinaryMatrix(copy.deepcopy(grid))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(grid)}x{len(grid)} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")
