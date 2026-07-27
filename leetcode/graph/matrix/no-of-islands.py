# Find the Number of Islands
# Prereq: BFS on Graph

# Given a 2-dimensional matrix of values with 0 and 1, count the number of islands of 1. An island consists of all 1 value cells and is surrounded by either an edge or all 0 cells. Cells can only be adjacent to each other horizontally or vertically, not diagonally.


from collections import deque

def count_number_of_islands(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    num_rows = len(grid)
    num_cols = len(grid[0])
    def get_neighbors(coord):
        res = []
        row,col = coord
        delta_row = [-1,0,1,0]
        delta_col = [0,1,0,-1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r,c))

        return res

    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 0:
                    continue
                queue.append(neighbor)
                grid[r][c] = 0

    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1  # bfs would find 1 connected island, increment count
    return count


# --- Daily tests ---
if __name__ == "__main__":
    import copy

    TESTS = [
        ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]], 3),
        ([[1, 0], [0, 1]], 2),
        ([[0]], 0),
    ]
    passed = 0
    for grid, exp in TESTS:
        got = count_number_of_islands(copy.deepcopy(grid))
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] grid -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

