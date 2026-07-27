# On an infinitely large chessboard, a knight is located on [0, 0].

# A knight can move in eight directions.



# Given a destination coordinate [x, y], determine the minimum number of moves from [0, 0] to [x, y].


from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    def get_neighbors(coord):
        res = []
        row,col = coord
        delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_col = [-1,  1,  2, 2, 1, -1, -2, -2]

        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            res.append((r,c))
        return res

    def bfs(start):
        visited = {start}
        steps = 0
        queue = deque([start])

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == (y,x):
                    return steps
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            steps += 1
        return steps

    return bfs((0,0))


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [(2, 1, 1), (5, 5, 4), (0, 0, 0)]
    passed = 0
    for x, y, exp in TESTS:
        got = get_knight_shortest_path(x, y)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] ({x},{y}) -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

