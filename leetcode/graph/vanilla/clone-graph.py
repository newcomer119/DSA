from collections import deque 

def clone_graph(adj_list: list[list[int]]) -> list[list[int]]:
    if not adj_list:
        return []
    n = len(adj_list)
    result = [[] for _ in range(n)]

    queue = deque([0])
    visited = {0}
    while queue:
        node = queue.popleft()
        result[node] = adj_list[node].copy()

        for neighbor in adj_list[node]:
            neighbor_idx = neighbor - 1
            if neighbor_idx < n and neighbor_idx not in visited:
                queue.append(neighbor_idx)
                visited.add(neighbor_idx)
    return result


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        ([[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]),
        ([[2], [1]], [[2], [1]]),
        ([], []),
    ]
    passed = 0
    for adj, exp in TESTS:
        got = clone_graph(adj)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {len(adj)} nodes -> ok")
    print(f"\n{passed}/{len(TESTS)} passed")

