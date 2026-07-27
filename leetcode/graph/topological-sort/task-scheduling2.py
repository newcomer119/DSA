# Task Scheduling 2
# Prereq: Topological Sort

# This problem extends Task Scheduling. Each task now has a duration, where times[i] is how long tasks[i] takes.

# You can run any number of tasks in parallel, as long as dependencies are respected. If [a, b] appears in requirements, task a must finish before task b can start.

# Return the minimum total time required to complete all tasks.

# There is guaranteed to be a solution.

# Examples
# Example 1
# Input:
# tasks = ["a", "b", "c", "d"]
# times = [1, 1, 2, 1]
# requirements = [["a", "b"], ["c", "b"], ["b", "d"]]
# Output: 4
# Figure
# Example 1 dependency graph with task durations

# The longest dependency chain is c -> b -> d, so the minimum total time is 2 + 1 + 1 = 4.


from collections import deque

def count_parents(graph: dict[str, list[str]]) -> dict[str, int]:
    counts = {node: 0 for node in graph}
    for parent in graph:
        for child in graph[parent]:
            counts[child] += 1
    return counts


def topo_sort(graph: dict[str, list[str]], task_times: dict[str, int]) -> int:
    q = deque()
    dis = {node: 0 for node in graph}  # earliest finish time
    indeg = count_parents(graph)

    ans = 0

    # start with tasks that have no prerequisites
    for node in indeg:
        if indeg[node] == 0:
            q.append(node)
            dis[node] = task_times[node]
            ans = max(ans, dis[node])

    while q:
        node = q.popleft()

        for child in graph[node]:
            # relax edge node -> child
            dis[child] = max(dis[child], dis[node] + task_times[child])
            ans = max(ans, dis[child])

            indeg[child] -= 1
            if indeg[child] == 0:
                q.append(child)

    return ans

def task_scheduling_2(tasks: list[str], times: list[int], requirements: list[list[str]]) -> int:
    graph: dict[str, list[str]] = {t: [] for t in tasks}
    task_times: dict[str, int] = {tasks[i]: times[i] for i in range(len(tasks))}

    for a, b in requirements:
        graph[a].append(b)

    return topo_sort(graph, task_times)


# --- Daily tests ---
if __name__ == "__main__":
    TESTS = [
        (["a", "b", "c", "d"], [1, 1, 2, 1], [["a", "b"], ["c", "b"], ["b", "d"]], 4),
        (["a", "b"], [3, 2], [["a", "b"]], 5),
        (["a", "b", "c"], [1, 1, 1], [["a", "b"], ["a", "c"]], 2),
    ]
    passed = 0
    for tasks, times, requirements, exp in TESTS:
        got = task_scheduling_2(tasks, times, requirements)
        ok = got == exp
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {tasks} -> {got}")
    print(f"\n{passed}/{len(TESTS)} passed")

