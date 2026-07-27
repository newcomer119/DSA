from collections import deque
from math import inf

def shortest_path(graph: list[list[tuple[int, int]]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    def bfs(root: int, target: int):

        queue = deque([root])
        distance = [inf] * len(graph)
        distance[root] = 0
        while queue: 
            node = queue.popleft()
            for neighb , weight in get_neighbors(node):
                if distance[neighb] <= distance[node] + weight:
                    continue
                queue.append(neighb)
                distance[neighb] = distance[node] + weight

        return distance[target]

    return -1 if bfs(a,b) == inf else bfs(a,b)


# --- Daily tests ---
if __name__ == "__main__":
    graph = [[(1, 1), (2, 4)], [(2, 2)], [(3, 1)], []]
    TESTS = [(0, 3, 4), (0, 1, 1), (1, 3, 3)]
    passed = 0
    for a, b, exp in TESTS:
        got = shortest_path(graph, a, b)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {a}->{b} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

