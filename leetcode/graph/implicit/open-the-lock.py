# You are faced with a 4-wheel lock where each wheel contains the numbers '0' through '9'. Turning a wheel can either increase or decrease its number by one, wrapping around from '9' to '0' or vice versa. A single move involves rotating any one of the wheels by one slot.

# The lock starts with the combination '0000'. However, there are specific combinations termed as "deadends". If the lock lands on any of these deadend combinations, the wheels jam, making it impossible to proceed.

# Your task is to determine the least number of moves needed to reach a given target combination from the starting point without hitting any deadend. If reaching the target is impossible due to deadends, return -1.

# Input & Output
# Input
# target_combo — a string representing the four digit combination to open the lock.
# trapped_combos — a list of strings representing the trapped combinations.
# Output
# An integer representing the number of steps it takes to open the lock, or `-1` if you can't open it without triggering the trap.
# Example
# Input
# target_combo = "0202"
# trapped_combos = ["0201","0101","0102","1212","2002"]
# Output
# 6
# Explanation
# 0000 -> 1000 -> 1100 -> 1200 -> 1201 -> 1202 -> 0202, a total of 6 steps.


from collections import deque

next_digit = {**{str(i) : str(i+1) for i in range(9)}, "9":"0"}
prev_digit = {e:n for n,e in next_digit.items()}


def num_steps(target_combo: str, trapped_combos: list[str]) -> int:
    trapped_combos_set = set(trapped_combos)
    visited = set(["0000"])

    def get_neighbors(combo):
        unvisited_neighbors = []
        for i in range(4):
            # Try next digit
            new_combo = combo[:i] + next_digit[combo[i]] + combo[i + 1 :]
            if new_combo not in trapped_combos and new_combo not in visited:
                unvisited_neighbors.append(new_combo)
                visited.add(new_combo)

            # prev digit 
            new_combo = combo[:i] + prev_digit[combo[i]] + combo[i + 1 :]
            if new_combo not in trapped_combos and new_combo not in visited:
                unvisited_neighbors.append(new_combo)
                visited.add(new_combo)

        return unvisited_neighbors

    queue = deque(["0000"])
    distance = 0
    while queue:
        n = len(queue)
        distance += 1
        for _ in range(n):
            combo = queue.popleft()
            for neighbor in get_neighbors(combo):
                if neighbor == target_combo:
                    return distance
                queue.append(neighbor)
    return -1


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ("0202", ["0201", "0101", "0102", "1212", "2002"], 6),
        ("0001", [], 1),
        ("8888", ["8887"], 8),
    ]
    passed = 0
    for target, trapped, exp in TESTS:
        got = num_steps(target, trapped)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] target={target} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

