from heapq import heappop, heappush
from math import inf

def shortest_path(graph: list[list[tuple[int, int]]], a: int, b: int) -> int:
    def get_neighbors(node):
        return graph[node]

    def dijkstra(root,target):
        queue = [(0, root)]
        distance = [inf] * len(graph)
        distance[root] = 0

        while queue:
            dist, node = heappop(queue)
            if dist > distance[node]:
                continue
            for neighbor , weight in get_neighbors(node):
                d = distance[node] + weight
                if distance[neighbor] <= d:
                    continue
                distance[neighbor] = d
                heappush(queue, (d, neighbor))

        return distance[target]

    res = dijkstra(a, b)
    return -1 if res == inf else res


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

