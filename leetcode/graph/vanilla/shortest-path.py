# Prereq: BFS on Graph

# Given an (unweighted) connected graph, return the length of the shortest path between two nodes A and B, in terms of the number of edges.

# Assume there always exists a path between nodes A and B.

# Input:

# graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
# A = 0
# B = 3
# Output: 2


# Note that the graph input is an adjacency list representation, not an adjacency matrix or a 2D grid. Specifically, graph[i] is the list of neighbor nodes for node i. For example, graph = [[1, 2], [0], [0]] means node 0 has edges to nodes 1 and 2. You can use the BFS template from BFS on Graphs as your starter code.
from collections import deque


def shortest_path(graph: list[list[int]], a: int, b: int) -> int:
    def get_neighbors(node):
        return graph[node]

    def bfs(root,target):
        queue = deque([root])
        visited = {root}
        level = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == target:
                    return level

                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue 

                    queue.append(neighbor)
                    visited.add(neighbor)

            level += 1
        return level

    # def bfs(root, target):
    #     queue = deque([root])
    #     visited = {root}
    #     level = 0
    #     while len(queue) > 0:
    #         n = len(queue)
    #         for _ in range(n):
    #             node = queue.popleft()
    #             if node == target:
    #                 return level
    #             for neighbor in get_neighbors(node):
    #                 if neighbor in visited:
    #                     continue
    #                 queue.append(neighbor)
    #                 visited.add(neighbor)

    #         level += 1
    #     return level
    return bfs(a, b)


# --- Daily tests ---
if __name__ == "__main__":
    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
    TESTS = [(0, 3, 2), (0, 2, 1), (0, 0, 0)]
    passed = 0
    for a, b, exp in TESTS:
        got = shortest_path(graph, a, b)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {a}->{b} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

