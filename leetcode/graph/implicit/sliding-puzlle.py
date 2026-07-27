# A sliding puzzle consists of a 2 x 3 board with tiles numbered 1 to 5 and one empty space represented by 0. The board is represented as a 2 x 3 matrix. For example:



# The configuration above is represented by [[4, 1, 3], [2, 0, 5]].

# Each move swaps the empty space with an adjacent tile (horizontally or vertically). The goal is to reach the solved state [[1, 2, 3], [4, 5, 0]]:



# Given an initial board configuration, find the minimum number of moves to reach the solved state, or return -1 if impossible.

# Input & Output
# Input
# init_pos — an integer matrix representing the initial position of the puzzle.
# Output
# The number of steps required to solve this puzzle, or `-1` if the puzzle is impossible to solve.
# Example
# Input
# init_pos = [[4, 1, 3], [2, 0, 5]]
# Output
# 5
# Constraints
# The input must be a 2 x 3 integer matrix containing exactly one of each from 0 to 5


from collections import deque
directions = [(1,0),(0,1),(-1,0),(0,-1)]
target = ((1,2,3), (4,5,0))

def num_steps(init_pos: list[list[int]]) -> int:
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0
    visited = set([init_pos])
    def get_neighbors(state):
        row,col =0,0
        for i, line in enumerate(state):
            for j,entry in enumerate(line):
                if entry == 0:
                    row,col = i,j

        unvisited_neighbors = []
        for delta_row,delta_col in directions:
            new_row,new_col = row + delta_row, col + delta_col
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_state = [list(line) for line in state]
                new_state[new_row][new_col] , new_state[row][col] = (new_state[row][col], new_state[new_row][new_col])
                new_tuple = tuple(tuple(line) for line in new_state)

                if new_tuple not in visited:
                    unvisited_neighbors.append(new_tuple)
                    visited.add(new_tuple)

        return unvisited_neighbors

    queue = deque([init_pos])
    distance = 0

    while queue:
        n = len(queue)
        distance += 1
        for _ in range(n):
            state = queue.popleft()
            for neighbor in get_neighbors(state):
                if neighbor == target:
                    return distance
                queue.append(neighbor)

    return -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[4, 1, 3], [2, 0, 5]], 5),
        ([[1, 2, 3], [4, 5, 0]], 0),
        ([[1, 2, 3], [5, 4, 0]], -1),
    ]
    passed = 0
    for board, exp in TESTS:
        got = num_steps(board)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {board} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

