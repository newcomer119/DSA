# Course Schedule
# Prereq: DFS on Graph
# There are a total of n courses a student has to take, numbered from 0 to n-1. A course may have prerequisites. The "depends on" relationship is expressed as a pair of numbers. For example, [0, 1] means you need to take course 1 before taking course 0. Given n and the list of prerequisites, decide if it is possible to take all the courses.
# Example 1:
# Input: n = 2, prerequisites = [[0, 1]]
# Output: true
# Explanation: we can take 1 first and then 0.
# Example 2:
# Input: n = 2, prerequisites = [[0, 1], [1, 0]]
# Output: false
# Explanation: the two courses depend on each other, there is no way to take them

from collections import deque
def count_parents(graph: dict[int, list[int]]) -> dict[int, int]:
    # Using your original logic to calculate indegree
    counts = {node: 0 for node in graph}
    for parent in graph:
        for child in graph[parent]:
            counts[child] += 1
    return counts

def is_valid_course_schedule(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(numCourses)}
    for dest, src in prerequisites:
        graph[src].append(dest)      
    # 2. Get the indegree for every node using your helper
    indeg = count_parents(graph)
    # 3. Queue with nodes that have 0 prerequisites (0 parents)
    q = deque([node for node in indeg if indeg[node] == 0])
    processed_count = 0
    # 4. BFS Traversal
    while q:
        node = q.popleft()
        processed_count += 1
        for child in graph[node]:
            # "Remove" the edge by decreasing indegree
            indeg[child] -= 1
            # If the child now has no prerequisites, it's ready
            if indeg[child] == 0:
                q.append(child)
                
    # 5. If we processed every course, no cycle existed
    return processed_count == numCourses


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (2, [[0, 1]], True),
        (2, [[0, 1], [1, 0]], False),
        (3, [[1, 0], [2, 0]], True),
    ]
    passed = 0
    for n, prereqs, exp in TESTS:
        got = is_valid_course_schedule(n, prereqs)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] n={n} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

