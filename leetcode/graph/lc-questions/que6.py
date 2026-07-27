

# Code
# Testcase
# Testcase
# Test Result
# 417. Pacific Atlantic Water Flow
# Solved
# Medium
# Topics
# premium lock icon
# Companies
from collections import deque
from typing import List

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def get_neighbors(r, c):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        def bfs(starts):
            q = deque(starts)
            visited = set(starts)

            while q:
                r, c = q.popleft()
                for nr, nc in get_neighbors(r, c):
                    if (nr, nc) in visited:
                        continue
                    # reverse-flow condition (ocean -> inland)
                    if heights[nr][nc] < heights[r][c]:
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))

            return visited

        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pac = bfs(pacific_starts)
        atl = bfs(atlantic_starts)

        ans =  [[r, c] for (r, c) in (pac & atl)]
        ans.sort()
        return ans


# --- Daily tests ---
if __name__ == "__main__":
    sol = Solution()
    TESTS = [
        (
            [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
        ([[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ]
    passed = 0
    for heights, exp in TESTS:
        got = sol.pacificAtlantic(heights)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(heights)}x{len(heights[0])} -> {len(got)} cells")
    print(f"\n{passed}/{len(TESTS)} passed")
