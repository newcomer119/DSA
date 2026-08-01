# Walls and Gates / Zombie in Matrix
# You are given an m by n grid of integers representing a map of a dungeon. In this map:

# -1 represents a wall or an obstacle of some kind.
# 0 represents a gate out of the dungeon.
# INF represents empty space.
# For this question, let INF be 2^31 - 1 == 2147483647, which is the max value of the integer type in many programming languages.

# Venturing into the dungeon is very dangerous, so you would like to know how close you are at each point in the dungeon to the closest exit. Given the map of the dungeon, return the same map, but for each empty space, that space is replaced by the number of steps it takes to reach the closest exit. If a space cannot reach the exit, that space remains INF.

# Note that each step, you can move horizontally or vertically, but you cannot move pass a wall or an obstacle.

# Input & Output
# Input
# dungeon_map — a matrix of integer representing the dungeon map.
# Output
# A matrix of integer representing the dungeon map with the addition of distance to an exit for each empty space.
# Example
# Input
# dungeon_map = [
#   [INF, -1, 0, INF],
#   [INF, INF, INF, -1],
#   [INF, -1, INF, -1],
#   [0, -1, INF, INF],
# ]
# Output
# [
#   [3, -1, 0, 1],
#   [2, 2, 1, -1],
#   [1, -1, 2, -1],
#   [0, -1, 3, 4],
# ]
# Constraints
# 1 <= n, m <= 500


from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 2147483647


def map_gate_distances(dungeon_map: list[list[int]]) -> list[list[int]]:
    queue =deque()
    n = len(dungeon_map)
    m = len(dungeon_map[0])

    for i,map_row in enumerate(dungeon_map):
        for j,entry in enumerate(map_row):
            if entry == 0:
                queue.append((i, j))

    while queue:
        r,c = queue.popleft()
        for dr,dc in directions:
            total_row = r + dr
            total_col = c + dc
            if total_row >= 0 and total_row < n and total_col >= 0 and total_col < m:
                if dungeon_map[total_row][total_col] == INF:
                    dungeon_map[total_row][total_col] = dungeon_map[r][c] + 1
                    queue.append((total_row, total_col))

    return dungeon_map
    
    # queue: deque[tuple[int, int]] = deque()
    # n = len(dungeon_map)
    # m = len(dungeon_map[0])
    # for i, map_row in enumerate(dungeon_map):
    #     for j, entry in enumerate(map_row):
    #         if entry == 0:
    #             queue.append((i, j))

    # while queue:
    #     row, col = queue.popleft()
    #     for delta_row, delta_col in directions:
    #         total_row, total_col = row + delta_row, col + delta_col
    #         if total_row >= 0 and total_row < n and total_col >= 0 and total_col < m:
    #             if dungeon_map[total_row][total_col] == INF:
    #                 dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
    #                 queue.append((total_row, total_col))

    # return dungeon_map


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (
            [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        ([[0]], [[0]]),
        ([[INF, 0], [INF, INF]], [[1, 0], [2, 1]]),
    ]
    passed = 0
    for dungeon, exp in TESTS:
        got = map_gate_distances([row[:] for row in dungeon])
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(dungeon)}x{len(dungeon[0])} -> ok")
    print(f"\n{passed}/{len(TESTS)} passed")

