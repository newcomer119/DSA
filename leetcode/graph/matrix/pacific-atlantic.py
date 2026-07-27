# There is an m x n rectangular island that borders both the Pacific Ocean and the Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches its right and bottom edges. You are given an m x n integer matrix heights where heights[r][c] is the height above sea level of the cell at coordinate (r, c).

# Rain water flows from a cell to a neighboring cell (north, south, east, or west) only when the neighbor's height is less than or equal to the current cell's height, and any cell adjacent to an ocean can drain into that ocean. Return a list of coordinates [r, c] for every cell from which water can flow to both the Pacific and Atlantic oceans.


# Toggle the views above to trace which cells drain to each ocean. The cells that reach both are the answer you must return.

# Input & Output
# Input
# heights — an m x n integer matrix representing the height above sea level of each cell
# Output
# a list of grid coordinates where rain water can flow to both oceans
# Example
# Input
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example
# Input
# heights = [[2,1],[1,2]]
# Output
# [[0,0],[0,1],[1,0],[1,1]]


from collections import deque


def pacific_atlantic_water_flow(heights: list[list[int]]) -> list[list[int]]:
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

    pacific_starts = [(0, c) for c in range(cols)] + [(r, 0)
                                                      for r in range(rows)]
    atlantic_starts = [(rows - 1, c) for c in range(cols)] + \
        [(r, cols - 1) for r in range(rows)]

    pac = bfs(pacific_starts)
    atl = bfs(atlantic_starts)

    ans = [[r, c] for (r, c) in (pac & atl)]
    ans.sort()
    return ans


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
        (
            [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ]
    passed = 0
    for heights, exp in TESTS:
        got = pacific_atlantic_water_flow(heights)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(heights)}x{len(heights[0])} -> {len(got)} cells")
    print(f"\n{passed}/{len(TESTS)} passed")

